# Infrastructure

This document describes the repositories, services, and deployment architecture used by Path Header Scanner.

## Overview

```text
Developer
    │
    ▼
GitHub (Primary Repository)
    │
    ├── Source Code
    ├── Issues
    ├── Releases
    ├── Tags
    └── Documentation Source
    │
    ├──────────────► GitHub Releases
    │                 ├── .whl
    │                 └── .tar.gz
    │
    ▼
GitLab (Mirror Repository)
    │
    ├── CI/CD
    ├── Linting
    ├── Testing
    └── Coverage Reports

Docker
    │
    └── Container Runtime

Docker Compose
    │
    └── Local Development

GitHub Pages
    │
    └── Documentation Site
```

---

## Platforms

| Purpose                 | Platform       |
| ----------------------- | -------------- |
| Source Code             | GitHub         |
| Releases                | GitHub         |
| Tags                    | GitHub         |
| Issues                  | GitHub         |
| Discussions             | GitHub         |
| Mirror Repository       | GitLab         |
| CI/CD                   | GitLab         |
| Coverage Reports        | GitLab         |
| Documentation           | GitHub Pages   |
| Container Registry      | GHCR           |
| Container Images        | Docker         |
| Container Orchestration | Docker Compose |

---

## Repository URLs

### GitHub (Primary)

https://github.com/devalltect00/Path-Header-Scanner

Responsibilities:

- Source of truth
- Pull requests
- Issues
- Releases
- Tags

### GitLab (Mirror)

https://gitlab.com/devalltects-group/path-header-scanner

Responsibilities:

- CI/CD pipelines
- Coverage reports
- Automated testing

---

## Documentation

Documentation is generated using:

- MkDocs
- Material for MkDocs

Published at:

https://devalltect00.github.io/Path-Header-Scanner/

---

## Installation & Distribution

Path Header Scanner can be installed using several methods.

### GitHub Repository

Install directly from GitHub:

```bash
pip install git+https://github.com/devalltect00/Path-Header-Scanner.git
```

Specific tag:

```bash
pip install git+https://github.com/devalltect00/Path-Header-Scanner.git@v1.0.0
```

---

### GitLab Repository

Install directly from GitLab:

```bash
pip install git+https://gitlab.com/devalltects-group/path-header-scanner.git
```

Specific tag:

```bash
pip install git+https://gitlab.com/devalltects-group/path-header-scanner.git@v1.0.0
```

---

### Release Artifacts

Release artifacts are generated using:

- build
- twine

Artifacts:

```text
dist/
├── *.whl
└── *.tar.gz
```

Install wheel:

```bash
pip install path_header_scanner-1.0.0-py3-none-any.whl
```

Install source distribution:

```bash
pip install path_header_scanner-1.0.0.tar.gz
```

---

### Docker

Build locally:

```bash
docker build -t path-header-scanner .
```

Run container:

```bash
docker run path-header-scanner
```

---

### Docker Compose

Run using Docker Compose:

```bash
docker compose up
```

or

```bash
docker compose up -d
```

---

## CI/CD Flow

```text
Push to GitHub
        │
        ▼
Mirror to GitLab
        │
        ▼
GitLab Pipeline
        │
        ├── Ruff
        ├── Black
        ├── Pytest
        └── Coverage
```

Current branch, version-tag, container, and provider-release behavior is
documented in [CI/CD and release contract](ci-cd.md).
