# Usage (Advanced Reference)

This page is the technical reference companion to:

- `docs/how-to-use.md` (primary beginner-friendly guide)

Use this page when you need command variants, execution context choices, and workflow mapping.

---

## Command model

```bash
path-header-scanner [OPTIONS] COMMAND [ARGS]...
```

Main commands:

- `init`
- `scan`

Global options:

- `--help`
- `--version`
- `--no-banner`

---

## `init` reference

```bash
path-header-scanner init --mode <mode> [--force] [--ask] [--dry-run]
```

Supported modes (from implementation):

- `all`
- `config`

Examples:

```bash
path-header-scanner init --mode all
path-header-scanner init --mode config --ask
path-header-scanner init --mode all --force
path-header-scanner init --dry-run
```

---

## `scan` reference

```bash
path-header-scanner scan TARGET_DIRECTORY [OPTIONS]
```

Supported options:

- `--workdir TEXT`
- `--apply`
- `--dry-run / --no-dry-run`
- `--debug`
- `--include-target-directory`
- `--exclude-target-directory`

Examples:

```bash
path-header-scanner scan app
path-header-scanner scan app --apply
path-header-scanner scan app --apply --dry-run
path-header-scanner scan app --debug
path-header-scanner scan src --workdir /workspace/project
path-header-scanner scan app --exclude-target-directory
```

---

## Execution contexts

### Local CLI

```bash
path-header-scanner scan app
```

### Python module mode

```bash
py -m app scan app
```

### Docker direct run

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" ghcr.io/devalltect00/path_header_scanner:<tag> scan app
```

### Docker Compose / Makefile workflows

Reference common automation from `Makefile`:

- Local:
    - `make l-scan TARGET=app`
    - `make l-scan-apply TARGET=app`
    - `make l-scan-debug TARGET=app`
- Docker:
    - `make d-scan TARGET=app`
    - `make d-scan-apply TARGET=app`
    - `make d-scan-debug TARGET=app`
- Compose:
    - `make c-scan TARGET=app`
    - `make c-scan-apply TARGET=app`
    - `make c-scan-debug TARGET=app`

---

## Safety and operational notes

Recommended sequence:

1. initialize once in target project (`init --mode all`)
2. run dry-run scan first
3. apply only after reviewing output

Explicit `--dry-run` overrides `--apply` and configured apply mode.

Example:

```bash
path-header-scanner init --mode all
path-header-scanner scan app
path-header-scanner scan app --apply
```

---

## Troubleshooting quick checks

1. verify command is available:
    ```bash
    path-header-scanner --help
    ```
2. verify target directory exists
3. retry with debug:
    ```bash
    path-header-scanner scan app --debug
    ```
4. confirm config exists:
    - `.config/path_header_scanner/config.toml`

---

## Exit behavior

- Success: exit code `0`
- Failure conditions: non-zero exit
- Known target, configuration, and filesystem failures include a concise reason and suggested correction.
- Unexpected implementation details and Python tracebacks are hidden from normal output. Retry `scan` with `--debug` and inspect the configured log file for technical diagnostics.
- Error handling does not weaken preview mode, `--apply`, or `--dry-run` safety.

---

## See also

- Beginner guide: `docs/how-to-use.md`
- Commands detail: `docs/user-guide/commands.md`
- Configuration: `docs/configuration.md`
- Dry-run safety: `docs/dry-run.md`
- Installation: `docs/installation.md`
