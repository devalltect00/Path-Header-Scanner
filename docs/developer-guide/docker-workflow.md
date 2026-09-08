<!-- docs/path-header/docker.md -->

# Docker Guide

This document explains Docker usage, development workflow, mounted workspaces, and containerized execution for Path Header Scanner.

---

# Overview

Path Header Scanner supports:

- direct Docker execution
- Docker Compose
- mounted workspace development
- CI/CD environments
- cross-platform execution

Benefits:

- isolated dependencies
- reproducible environments
- easier onboarding
- portable development workflow
- simplified CI integration

---

# Docker Concepts

| Concept | Meaning |
|---|---|
| Dockerfile | Build instructions for image creation |
| Image | Packaged application environment |
| Container | Running image instance |
| Docker Compose | Multi-container orchestration |
| Mounted Volume | Shared filesystem between host and container |

---

# Project Docker Architecture

## Components

| File | Responsibility |
|---|---|
| `Dockerfile` | Build application image |
| `docker-compose.yml` | Service orchestration |
| `Makefile` | Developer workflow shortcuts |

---

# Docker Build

# Build Using Docker

```bash
docker build -t path-header-scanner .
```

---

# Build Using Docker Compose

```bash
docker compose build
```

---

# Verify Image

```bash
docker images
```

Example:

```text
REPOSITORY             TAG       IMAGE ID
path-header-scanner    latest    xxxxxxxxxxxx
```

---

# Basic Docker Execution

# Dry Run

## Windows CMD

```cmd
docker run -it --rm -w /workspace -v "%cd%:/workspace" path-header-scanner scan app
```

## PowerShell

```powershell
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app
```

## Bash / Linux / macOS

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app
```

---

# Apply Changes

## Windows CMD

```cmd
docker run -it --rm -w /workspace -v "%cd%:/workspace" path-header-scanner scan app --apply
```

## Bash / Linux / macOS

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app --apply
```

---

# Debug Mode

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app --debug
```

---

# Exclude Target Directory

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app --exclude-target-directory
```

---

# Include Target Directory

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app --include-target-directory
```

---

# Understanding Docker Arguments

Example:

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app --debug
```

---

# Argument Breakdown

| Argument | Purpose |
|---|---|
| `docker run` | Start container |
| `-it` | Interactive terminal |
| `--rm` | Remove container after exit |
| `-w /workspace` | Set working directory |
| `-v "${PWD}:/workspace"` | Mount local project |
| `path-header-scanner` | Docker image name |
| `scan app` | Scanner command |
| `--debug` | Enable debug logging |

---

# Why `-w /workspace` Matters

Using:

```bash
-w /workspace
```

ensures:

- relative paths resolve correctly
- mounted workspace becomes runtime root
- simpler CLI commands
- cleaner path handling

Without it:

```bash
scan app
```

may resolve unexpectedly depending on container runtime directory.

---

# Mounted Workspace

The mounted volume:

```bash
-v "${PWD}:/workspace"
```

maps:

| Host | Container |
|---|---|
| Local project directory | `/workspace` |

This means:

- container changes affect local files
- scanner updates local source code directly
- no file copying required

---

# Docker Compose Usage

# Dry Run

```bash
docker compose run --rm \
    path-header-scanner \
    scan app
```

---

# Apply Changes

```bash
docker compose run --rm \
    path-header-scanner \
    scan app --apply
```

---

# Debug Mode

```bash
docker compose run --rm \
    path-header-scanner \
    scan app --debug
```

---

# Exclude Target Directory

```bash
docker compose run --rm \
    path-header-scanner \
    scan app --exclude-target-directory
```

---

# Interactive Shell

```bash
docker compose run --rm \
    path-header-scanner \
    bash
```

---

# Container Lifecycle

Typical execution flow:

```text
build image
↓
start container
↓
mount workspace
↓
execute CLI command
↓
modify files
↓
container removed
```

---

# Docker Compose Architecture

Typical compose structure:

```yaml
services:
  path-header-scanner:
    build: .
    working_dir: /workspace

    volumes:
      - .:/workspace
```

---

# Why Docker Compose?

Benefits:

- reusable configuration
- cleaner commands
- shared team workflow
- easier CI integration

---

# Makefile Integration

The project uses modular Make helpers for local, Docker, Compose, and published
image execution. Run `make help-docker` or `make help-compose` for the current
grouped command reference.

---

# Build Images

```bash
make d-build-all
```

---

# Dry Run

```bash
make d-scan TARGET=app
```

---

# Apply Changes

```bash
make d-scan-apply TARGET=app
```

---

# Debug Mode

```bash
make d-scan-debug TARGET=app
```

---

# Custom Target

```bash
make c-scan TARGET=src
```

See [`make-workflow.md`](make-workflow.md) for all command groups, shared
variables, and published utility image examples.

---

# Why `$(CURDIR)` Works

`$(CURDIR)` is a GNU Make built-in variable.

Equivalent variables:

| Environment | Variable |
|---|---|
| CMD | `%cd%` |
| PowerShell | `${PWD}` |
| Bash | `$PWD` |
| Make | `$(CURDIR)` |

Benefits:

- cross-platform
- shell-independent
- handled directly by Make

---

# Docker Path Resolution

Inside Docker:

```text
/workspace
```

acts as the runtime project root.

Examples:

| Local Path | Container Path |
|---|---|
| `C:\\project\\app` | `/workspace/app` |
| `./src` | `/workspace/src` |

---

# Working Directory Support

The scanner supports:

```bash
--workdir
```

Example:

```bash
path-header-scanner scan src \
    --workdir /workspace/project
```

Useful for:

- monorepos
- nested projects
- custom CI layouts

---

# Docker Logging

Recommended modes:

| Mode | Purpose |
|---|---|
| INFO | normal usage |
| DEBUG | troubleshooting |

Debug mode:

```bash
--debug
```

shows:

- resolved paths
- runtime directories
- processed files
- diagnostics

---

# CI/CD Usage

# GitHub Actions Example

```yaml
- name: Build Docker Image
  run: docker build -t path-header-scanner .

- name: Run Scanner
  run: |
    docker run --rm \
      -w /workspace \
      -v "${PWD}:/workspace" \
      path-header-scanner \
      scan app
```

---

# GitLab CI Example

```yaml
scan:
  script:
    - docker build -t path-header-scanner .
    - >
      docker run --rm
      -w /workspace
      -v "$PWD:/workspace"
      path-header-scanner
      scan app
```

---

# Common Docker Commands

# List Containers

```bash
docker ps
```

---

# List Images

```bash
docker images
```

---

# Remove Image

```bash
docker rmi path-header-scanner
```

---

# Cleanup Unused Resources

```bash
docker system prune -f
```

---

# Common Issues

# Permission Problems

Linux/macOS may require:

```bash
sudo
```

depending on Docker installation.

---

# Mounted Files Not Updating

Verify volume mount:

```bash
-v "${PWD}:/workspace"
```

---

# Wrong Relative Paths

Ensure:

```bash
-w /workspace
```

is provided.

---

# Image Not Found

Build image first:

```bash
docker build -t path-header-scanner .
```

---

# Best Practices

Recommended workflow:

1. build image once
2. use mounted workspace
3. use dry-run first
4. apply changes afterward
5. use Makefile shortcuts

---

# Recommended Development Flow

## Step 1

Build image:

```bash
make docker-build
```

## Step 2

Dry run:

```bash
make docker-scan
```

## Step 3

Review output.

## Step 4

Apply changes:

```bash
make docker-apply
```

---

# Notes

- Containers are ephemeral when using `--rm`.
- Mounted volumes allow direct local file updates.
- Docker support is optimized for workspace-based development.
- Relative path handling is designed for mounted environments.
- Docker Compose simplifies team onboarding and CI workflows.

Stable production releases publish four coordinated references to the same
image: exact `v1.0.0`, minor `v1.0`, major `v1`, and `latest`. Pin CI and
reproducible automation to the immutable exact tag. The other aliases move only
when a compatible stable release is published. Prereleases such as
`v1.0.0-rc.1` publish only their exact tag.

See [CI/CD and release contract](../ci-cd.md) for dynamic registry naming,
annotated release tags, provider parity, and stable alias safeguards.
