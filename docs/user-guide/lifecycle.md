<!-- docs/user-guide/lifecycle.md -->

# User Lifecycle Guide (Start, Run, Stop, Exit, Remove)

This guide helps users operate the tool end-to-end with minimal confusion.

## 1) Start

From your project root:

```bash
path-header-scanner --help
path-header-scanner init
```

Initialization sets up project-local defaults/config artifacts for the tool.

## 2) Run safely (dry run first)

```bash
path-header-scanner scan app
```

Dry-run lets you inspect what would happen before writing files.

## 3) Run with write/apply

```bash
path-header-scanner scan app --apply
```

This updates file headers in the scanned directory.

## 4) Debug run

```bash
path-header-scanner scan app --debug
```

Use debug when diagnosing path resolution or processing behavior.

## 5) Stop / Exit

- Local CLI: press `Ctrl+C` to stop running command
- Docker container with `--rm`: exits and removes container automatically

## 6) Remove / clean up

### Uninstall package (if installed via pip)

```bash
pip uninstall path-header-scanner
```

### Remove Docker images (if docker-based usage)

```bash
docker images
docker rmi ghcr.io/devalltect00/path_header_scanner:<tag>
```

### Remove generated local artifacts (optional, caution)

If you want to reset local setup, remove generated config directory in your target project (only if you know you no longer need it):

```text
.config/path_header_scanner/
```

## 7) Recommended next action after `init`

1. run dry-run scan
2. review output
3. run `--apply`
4. commit changed files to version control

## 8) Where to get more docs

- User docs index: `docs/user-guide/overview.md`
- Full usage: `docs/usage.md` (protected)
- Configuration options: `docs/configuration.md` (protected)
