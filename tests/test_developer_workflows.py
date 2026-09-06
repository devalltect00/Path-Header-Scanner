# tests/test_developer_workflows.py

"""Structural regression tests for Path Header Scanner developer workflows."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    """Read a project file as UTF-8 text."""

    return (PROJECT_ROOT / relative_path).read_text(encoding="utf-8")


def test_modular_make_workflows_are_installed() -> None:
    """Keep the root Makefile small and load all workflow modules."""

    makefile = _read("Makefile")
    assert "include make/core/variables/variable.mk" in makefile
    assert "include make/core/local/command.mk" in makefile
    assert "include make/core/remote/command/runtime.mk" in makefile
    assert "include make/core/help/command.mk" in makefile

    local_commands = _read("make/core/local/command.mk")
    assert "l-scan-apply" in local_commands
    assert "--apply" in local_commands
    assert "l-scan-apply-all" in local_commands
    assert "for %%t in ($(PHS_SCAN_TARGETS))" in local_commands
    assert 'TARGET="$$target"' in local_commands


def test_development_helpers_reuse_the_app_image() -> None:
    """Only the development app service should own the build definition."""

    compose = _read("docker-compose.dev.yml")
    assert "x-development-service: &development-service" in compose
    assert compose.count("build: *development-build") == 1
    assert compose.count("<<: *development-service") == 10
    assert "extends:\n      service: app" not in compose


def test_dockerfile_validates_runtime_and_accepts_an_explicit_version() -> None:
    """Container builds should validate imports and support SCM version injection."""

    dockerfile = _read("Dockerfile")
    assert "ARG PHS_BUILD_VERSION" in dockerfile
    assert dockerfile.count("SETUPTOOLS_SCM_PRETEND_VERSION") == 2
    assert 'RUN python -c "from app.cli.main import app"' in dockerfile


def test_published_images_receive_the_scm_package_version() -> None:
    """Published development and production images should retain package versions."""

    development = _read(".github/workflows/docker-dev.yml")
    production = _read(".github/workflows/docker-prod.yml")

    assert "python -m app.core.build.version" in development
    assert "PHS_BUILD_VERSION=${{ steps.package-version.outputs.value }}" in development
    assert "python -m app.core.build.version" in production
    assert "PHS_BUILD_VERSION=${{ steps.version.outputs.version }}" in production


def test_release_workflows_enforce_reviewed_tag_publication() -> None:
    """Hosted workflows should publish only reviewed stable or prerelease tags."""

    production = _read(".github/workflows/docker-prod.yml")
    release = _read(".github/workflows/release.yml")
    gitlab_development = _read(".gitlab/docker-dev.yml")
    gitlab_production = _read(".gitlab/docker-prod.yml")
    gitlab_release = _read(".gitlab/release.yml")
    gitlab_package = _read(".gitlab/python-package.yml")

    for text in (production, release):
        assert "annotated Git tag" in text
        assert "rc|dev|post" in text

    assert "annotated Git tag" in gitlab_package
    assert "CI_COMMIT_REF_PROTECTED" in gitlab_package
    assert "CI_JOB_TOKEN" in gitlab_package
    assert "scripts/ci/package_version.py" in gitlab_package
    assert (
        "Unprotected tag detected; validating package artifacts only" in gitlab_package
    )
    assert "publication requires a protected release tag" not in gitlab_package

    assert "branches:" not in production
    assert "steps.vars.outputs.image_name" in production
    assert "publish_latest" in production
    assert "type=sha" not in production
    assert "docker/dev/Dockerfile" not in gitlab_development
    assert "docker/prod/Dockerfile" not in gitlab_production
    assert "--target development" in gitlab_development
    assert "--target production" in gitlab_production
    assert "job: package:build" in gitlab_production
    assert "job: package:publish" in gitlab_release
    assert "job: docker:prod" in gitlab_release
    for protected_workflow in (
        gitlab_package,
        gitlab_production,
        gitlab_release,
    ):
        assert 'CI_COMMIT_REF_PROTECTED == "true"' in protected_workflow
    assert 'description: "./RELEASE_NOTES.md"' in gitlab_release
    assert "\\`$PACKAGE_VERSION\\`" in gitlab_release
    assert "      ```bash" not in gitlab_release

    # Markdown backticks inside an unquoted heredoc are Bash command
    # substitutions. Release-note generation must keep Docker examples literal.
    assert "cat <<EOF >> RELEASE_NOTES.md" not in release
    assert "printf '```bash\\n'" in release
    assert "docker pull ghcr.io/%s:%s\\n" in release
    assert "docker run --rm ghcr.io/%s:%s --help\\n" in release
    assert '"$IMAGE_NAME" "$IMAGE_TAG"' in release
    assert "- Version: `%s`\\n" in release
    assert "- Release Type: `%s`\\n" in release
    assert '"$GITHUB_REPOSITORY"' in release
    assert '"$GITHUB_WORKFLOW"' in release


def test_gitlab_pipeline_publishes_validated_private_python_packages() -> None:
    """The modular pipeline should publish immutable packages before release."""

    pipeline = _read(".gitlab-ci.yml")
    package = _read(".gitlab/python-package.yml")

    for stage in ("test", "package", "docker", "publish", "release"):
        assert f"  - {stage}" in pipeline
    assert 'local: ".gitlab/python-package.yml"' in pipeline
    assert "python -m twine check dist/*" in package
    assert "SETUPTOOLS_SCM_PRETEND_VERSION" in package
    assert "--repository-url" in package
    assert "--skip-existing" not in package


def test_ignore_files_cover_local_test_workspaces() -> None:
    """Local Pytest workspaces should stay outside Git and image contexts."""

    for ignore_file in (".gitignore", ".dockerignore"):
        text = _read(ignore_file)
        assert ".pytest-tmp-*/" in text
        assert "\n/build/\n" in text

    assert ".config/path_header_scanner/config.toml" in _read(".dockerignore")
