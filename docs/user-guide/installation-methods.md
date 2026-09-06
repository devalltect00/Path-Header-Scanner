<!-- docs/user-guide/installation-methods.md -->

# Installation Methods (User-Friendly)

This page summarizes practical installation choices.

For canonical installation details, also see protected doc:

- `docs/installation.md`

## Requirements

Depending on method, you may need:

- Python 3.11+ (Python 3.14 is the standard development and container runtime)
- pip
- Docker (optional)
- Make (optional, if using Makefile commands)
- Git (optional, if installing from repository source)

---

## Method 1: Python package (recommended for local developer machines)

Install from source repository:

```bash
pip install -e .[dev]
```

Validate:

```bash
path-header-scanner --help
```

Alternative module execution:

```bash
py -m app --help
```

---

## Method 2: Private GitLab PyPI registry

Use a deploy token with `read_package_registry` permission:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "path-header-scanner==1.0.0"
```

For a release-candidate tag such as `v1.0.0-rc.1`, install the normalized
package version explicitly:

```bash
python -m pip install \
  --index-url "https://<deploy-token-user>:<deploy-token>@gitlab.com/api/v4/projects/<project-id>/packages/pypi/simple" \
  "path-header-scanner==1.0.0rc1"
```

Do not commit tokens. Disable GitLab package forwarding when package resolution
must remain strictly private, and avoid `--extra-index-url` for private package
names.

---

## Method 3: Install from release assets (`.whl` or `.tar.gz`)

From GitHub Releases (example page):

- `https://github.com/devalltect00/Path-Header-Scanner/releases/tag/v1.0.7`

Download one asset such as:

- `path_header_scanner-<version>-py3-none-any.whl`
- `path_header_scanner-<version>.tar.gz`

Install:

```bash
pip install ./path_header_scanner-<version>-py3-none-any.whl
```

or:

```bash
pip install ./path_header_scanner-<version>.tar.gz
```

---

## Method 4: Docker image

Example pull command format:

```bash
docker pull ghcr.io/devalltect00/path_header_scanner:<tag>
```

Example run:

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" ghcr.io/devalltect00/path_header_scanner:<tag> --help
```

---

## Method 5: Makefile helpers (if available in your environment)

Prerequisite: `make` installed.

Common targets may include:

```bash
make docker-build
make docker-scan
make docker-apply
make docker-debug
```

---

## After install: recommended first commands

```bash
path-header-scanner --help
path-header-scanner init
path-header-scanner scan app
```

Then apply changes when ready:

```bash
path-header-scanner scan app --apply
```
