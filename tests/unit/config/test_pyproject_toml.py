# tests/unit/config/test_pyproject_toml.py

import tomllib
from pathlib import Path


def load_pyproject() -> dict:
    pyproject_file = Path("pyproject.toml")

    assert pyproject_file.exists(), "pyproject.toml does not exist"

    return tomllib.loads(
        pyproject_file.read_text(
            encoding="utf-8",
        )
    )


def test_pyproject_exists() -> None:
    assert Path("pyproject.toml").exists()


def test_pyproject_is_valid_toml() -> None:
    data = load_pyproject()

    assert isinstance(data, dict)


def test_project_metadata_exists() -> None:
    data = load_pyproject()

    project = data["project"]

    assert project["name"]
    assert project.get("version") or "version" in project.get("dynamic", [])
    assert project["requires-python"]


def test_click_is_a_direct_runtime_dependency() -> None:
    """Declare Click because the scanner imports its exception classes directly."""
    dependencies = load_pyproject()["project"]["dependencies"]

    assert any(dependency.startswith("click") for dependency in dependencies)


def test_project_metadata_describes_current_scanner_scope() -> None:
    """Keep published metadata aligned with supported scanner behavior."""
    project = load_pyproject()["project"]

    assert "previewing" in project["description"]
    assert "validating" in project["description"]
    assert "updating path headers" in project["description"]
    assert {
        "path-header",
        "header-scanner",
        "file-header",
        "code-maintenance",
        "dry-run",
        "typer",
        "rich",
        "docker",
    } <= set(project["keywords"])
    assert "Programming Language :: Python :: 3 :: Only" in project["classifiers"]


def test_project_urls_exist() -> None:
    data = load_pyproject()

    urls = data["project"]["urls"]

    assert {
        "Homepage",
        "Repository",
        "Issues",
        "Documentation",
        "Changelog",
        "Discussions",
        "Releases",
        "GitHub Actions",
        "GitLab CI",
        "Container Images",
    } <= urls.keys()
    assert all(url.startswith("https://") for url in urls.values())


def test_console_script_exists() -> None:
    data = load_pyproject()

    scripts = data["project"]["scripts"]

    assert "path-header-scanner" in scripts


def test_pytest_configuration_exists() -> None:
    data = load_pyproject()

    tool = data["tool"]

    assert "pytest" in tool


def test_black_configuration_exists() -> None:
    data = load_pyproject()

    tool = data["tool"]

    assert "black" in tool


def test_ruff_configuration_exists() -> None:
    data = load_pyproject()

    tool = data["tool"]

    assert "ruff" in tool


def test_coverage_configuration_exists() -> None:
    data = load_pyproject()

    tool = data["tool"]

    assert "coverage" in tool


def test_build_system_configuration_exists() -> None:
    data = load_pyproject()

    assert "build-system" in data


def test_dev_dependency_group_exists() -> None:
    data = load_pyproject()

    optional_deps = data["project"]["optional-dependencies"]

    assert "dev" in optional_deps


def test_docs_dependency_group_exists() -> None:
    data = load_pyproject()

    optional_deps = data["project"]["optional-dependencies"]

    assert "docs" in optional_deps
