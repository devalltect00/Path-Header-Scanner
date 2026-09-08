# CI/CD and release contract

Path Header Scanner validates ordinary development separately from production
publication. Branch and merge-request jobs may test code or publish development
images; production images and provider releases require a reviewed annotated tag.

## Trigger matrix

| Workflow | Trigger | External effect |
| --- | --- | --- |
| CI | `main`, `develop`, merge requests, and every pushed tag | None |
| Python package gate | Any tag | Validates the annotated tag and smoke-tests canonical PEP 440 artifacts without publishing |
| Development image | `develop` or `dev` | Publishes `dev` and commit-SHA tags |
| Production image | Validated protected release tag | Publishes the exact tag; stable releases also update matching minor, major, and `latest` aliases |
| Private Python package | Validated protected release tag | Publishes an immutable wheel and sdist to GitLab's project PyPI registry |
| Provider release | Validated protected release tag | Creates a release after image and package publication |

CI tests Python 3.11, the package compatibility floor, and Python 3.14, the
standard development and container runtime.

## Release safeguards

The package gate requires a supported release tag, an annotated tag object, a
non-empty tag message, and package artifacts whose filenames and embedded
metadata agree with the normalized version. An unprotected tag completes this
validation without failing, but its production image, package upload, and
release jobs are skipped. Those external publication jobs additionally require
GitLab protected-tag status. Manual GitHub runs select an existing tag; they do
not create one.

GitHub images use `ghcr.io/<owner>/<repository>:<tag>`. GitLab uses
`$CI_REGISTRY_IMAGE:<tag>`. Forks and disposable repositories therefore remain
inside their own registry namespace. Prereleases never update stable aliases.

A stable `v1.0.0` release publishes `v1.0.0`, `v1.0`, `v1`, and `latest`.
Use the immutable exact tag for reproducible automation. Minor, major, and
`latest` are intentionally moving aliases. Prereleases remain exact-only and
cannot move any stable alias.

The complete annotated tag message becomes the public provider release
description. Wheel and source-distribution artifacts are attached or linked.

## GitLab package version policy

`.gitlab/python-package.yml` converts supported SemVer spellings to canonical
PEP 440 before building the private Python package:

| Release tag | Package version |
| --- | --- |
| `v1.0.0` | `1.0.0` |
| `v1.0.0-alpha.1` | `1.0.0a1` |
| `v1.0.0-beta.1` | `1.0.0b1` |
| `v1.0.0-rc.1` | `1.0.0rc1` |
| `v1.0.0-dev.1` | `1.0.0.dev1` |
| `v1.0.0.post1` | `1.0.0.post1` |

Canonical PEP 440 tags are accepted too. Unknown labels, missing numeric
identifiers, build metadata, and ambiguous `-post.N` tags fail before any
publication. GitLab versions are immutable, so duplicate uploads fail rather
than overwriting or silently skipping existing packages.

The upload uses the short-lived `CI_JOB_TOKEN`. Maintainers must protect release
tag patterns in GitLab; consumers should use a deploy token with
`read_package_registry`. For strictly private resolution, disable package
forwarding in the GitLab group settings.

## Planned 1.0 message sequence

1. Use `commit-message-v1.0.0-development-checkpoint.txt` for the comprehensive product commit; do not tag it.
2. Use `commit-message-v1.0.0-rc.1.txt` for the CI/CD-finalization commit.
3. Create the annotated RC.1 tag from `tag-message-v1.0.0-rc.1.txt` on that commit.
4. After RC validation, commit the stable-image alias work with `commit-message-v1.0.0-stabilization-checkpoint.txt`; do not tag it.
5. After final cleanup, use `commit-message-v1.0.0.txt` for stable promotion.
6. Create the annotated stable tag from `tag-message-v1.0.0.txt`.

Development and stabilization checkpoints have no tag-message templates because they are intentionally not releases.

## Local validation

```bash
make check-ci
python -m app.core.build.version
docker compose -f docker-compose.yml -f docker-compose.dev.yml config
docker compose -f docker-compose.yml -f docker-compose.prod.yml config
```

These commands do not publish images or releases. Do not validate tag-triggered
publication against a production repository without separate approval.
