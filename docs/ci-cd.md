# CI/CD and release contract

Path Header Scanner validates ordinary development separately from production
publication. Branch and merge-request jobs may test code or publish development
images; production images and provider releases require a reviewed annotated tag.

## Trigger matrix

| Workflow | Trigger | External effect |
| --- | --- | --- |
| CI | `main`, `develop`, merge requests, and supported version tags | None |
| Development image | `develop` or `dev` | Publishes `dev` and commit-SHA tags |
| Production image | Existing annotated `v*` release tag | Publishes the exact tag; stable releases also update `latest` |
| Provider release | Existing annotated `v*` release tag | Creates a release with Python artifacts |

CI tests Python 3.11, the package compatibility floor, and Python 3.14, the
standard development and container runtime.

## Release safeguards

Production jobs require a supported SemVer-oriented tag such as `v1.0.0` or
`v1.0.0-rc.1`, an annotated tag object, a non-empty tag message, and a package
version that agrees with the tag. Manual GitHub runs select an existing tag;
they do not create one.

GitHub images use `ghcr.io/<owner>/<repository>:<tag>`. GitLab uses
`$CI_REGISTRY_IMAGE:<tag>`. Forks and disposable repositories therefore remain
inside their own registry namespace. Prereleases never update `latest`.

The complete annotated tag message becomes the public provider release
description. Wheel and source-distribution artifacts are attached or linked.

## Planned 1.0 message sequence

1. Use `commit-message-v1.0.0-development-checkpoint.txt` for the comprehensive product commit; do not tag it.
2. Use `commit-message-v1.0.0-rc.1.txt` for the CI/CD-finalization commit.
3. Create the annotated RC.1 tag from `tag-message-v1.0.0-rc.1.txt` on that commit.
4. After RC validation and cleanup, use `commit-message-v1.0.0.txt` for stable promotion.
5. Create the annotated stable tag from `tag-message-v1.0.0.txt`.

The checkpoint has no tag-message template because it is intentionally not a release.

## Local validation

```bash
make check-ci
python -m app.core.build.version
docker compose -f docker-compose.yml -f docker-compose.dev.yml config
docker compose -f docker-compose.yml -f docker-compose.prod.yml config
```

These commands do not publish images or releases. Do not validate tag-triggered
publication against a production repository without separate approval.
