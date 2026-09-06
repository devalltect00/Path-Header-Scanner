<!-- docs/how-to-use.md -->

# How to Use Path Header Scanner

This is the main practical usage guide for running Path Header Scanner in real projects.

This document is user-friendly and focused on:

- quick setup
- common command usage
- safe run flow
- how to stop or clean up

For advanced details, also see:

- `docs/usage.md`
- `docs/user-guide/commands.md`
- `docs/configuration.md`

---

## 1) Verify installation

Run:

```bash
path-header-scanner --help
```

Alternative module mode:

```bash
py -m app --help
```

If command is not found, install using one method from:

- `docs/installation.md`
- `docs/user-guide/installation-methods.md`

---

## 2) Initialize once per target project

From your target project root:

```bash
path-header-scanner init --mode all
```

Current implementation supports:

- `--mode all`
- `--mode config`

Optional behavior flags:

- `--force` (overwrite without prompt)
- `--ask` (ask before overwrite)
- `--dry-run` (preview without creating or overwriting files)

Example:

```bash
path-header-scanner init --mode config --ask
path-header-scanner init --mode config --dry-run
```

---

## 3) Run scan in dry-run mode first (recommended)

```bash
path-header-scanner scan app
```

Dry-run means no files are modified.

Use this to check what would change.

The equivalent explicit form is:

```bash
path-header-scanner scan app --dry-run
```

If `--apply` is also present, dry-run wins and the files remain unchanged.

---

## 4) Apply changes when results look correct

```bash
path-header-scanner scan app --apply
```

This writes header updates to files.

---

## 5) Useful scan options

Use custom working directory:

```bash
path-header-scanner scan src --workdir /workspace/project
```

Enable debug logging:

```bash
path-header-scanner scan app --debug
```

Exclude target directory from generated headers:

```bash
path-header-scanner scan app --exclude-target-directory
```

Include target directory in generated headers:

```bash
path-header-scanner scan app --include-target-directory
```

---

## 6) Typical workflows

### Local project flow

```bash
path-header-scanner init --mode all
path-header-scanner scan app
path-header-scanner scan app --apply
```

### Scan tests directory too

```bash
path-header-scanner scan tests
path-header-scanner scan tests --apply
```

### Show command help anytime

```bash
path-header-scanner --help
path-header-scanner init --help
path-header-scanner scan --help
```

---

## 7) Docker usage (example)

Pull release image:

```bash
docker pull ghcr.io/devalltect00/path_header_scanner:<tag>
```

Run help:

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" ghcr.io/devalltect00/path_header_scanner:<tag> --help
```

Run scan:

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" ghcr.io/devalltect00/path_header_scanner:<tag> scan app
```

Apply:

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" ghcr.io/devalltect00/path_header_scanner:<tag> scan app --apply
```

---

## 8) Stop / exit / cleanup

- Local command: press `Ctrl+C` to stop current execution.
- Docker with `--rm`: container is removed automatically on exit.

Optional cleanup:

```bash
pip uninstall path-header-scanner
docker rmi ghcr.io/devalltect00/path_header_scanner:<tag>
```

If you need to reset generated config in a target project, remove:

```text
.config/path_header_scanner/
```

(only if you intentionally want to reset setup)

---

## 9) Requirements checklist

Depending on your installation/run method:

- Python 3.11+ (Python 3.14 is the standard development and container runtime)
- pip
- Docker (optional)
- make (optional)
- git (optional)

---

## 10) Recommended next reading

- `docs/user-guide/overview.md`
- `docs/user-guide/quickstart.md`
- `docs/user-guide/commands.md`
- `docs/user-guide/lifecycle.md`
- `docs/configuration.md`
