<!-- docs/user-guide/commands.md -->

# Commands Reference

This page explains practical CLI command usage for users.

## Main command

```bash
path-header-scanner [OPTIONS] COMMAND [ARGS]...
```

Common global flags:

- `--help`
- `--no-banner`
- `--version`

---

## `init` command

Initialize project setup for Path Header Scanner usage.

```bash
path-header-scanner init [OPTIONS]
```

### Options

- `--mode [config|templates|examples|all]`
- `--force`
- `--ask`

### Examples

```bash
path-header-scanner init
path-header-scanner init --mode config
path-header-scanner init --force
path-header-scanner init --mode all --ask
```

---

## `scan` command

Scan and process source files for path headers.

```bash
path-header-scanner scan TARGET_DIRECTORY [OPTIONS]
```

### Argument

- `TARGET_DIRECTORY`: directory to scan recursively

### Options

- `--workdir TEXT`
- `--apply`
- `--debug`
- `--include-target-directory`
- `--exclude-target-directory`

### Examples

Dry run:

```bash
path-header-scanner scan app
```

Apply changes:

```bash
path-header-scanner scan app --apply
```

Use custom workdir:

```bash
path-header-scanner scan src --workdir /workspace/project
```

Exclude target directory in generated headers:

```bash
path-header-scanner scan app --exclude-target-directory
```

Include target directory in generated headers:

```bash
path-header-scanner scan app --include-target-directory
```

---

## Header behavior examples

Include target directory (default-like behavior in many workflows):

```python
# app/cli/main.py
```

Exclude target directory:

```python
# cli/main.py
```

---

## Help and troubleshooting shortcuts

```bash
path-header-scanner --help
path-header-scanner init --help
path-header-scanner scan --help
```

If a command fails:

1. check you are in the correct project directory
2. verify target directory exists
3. retry with `--debug`
4. validate configuration in `.config/path_header_scanner/config.toml`
