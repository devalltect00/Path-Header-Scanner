<!-- docs/user-guide/quickstart.md -->

# Quick Start

This is the fastest safe path to start using Path Header Scanner.

## 1) Install

Choose one installation path from:

- `docs/installation.md` (protected core install doc)
- `docs/user-guide/installation-methods.md` (expanded user-focused options)

## 2) Verify CLI

```bash
path-header-scanner --help
```

or module mode:

```bash
py -m app --help
```

## 3) Initialize project setup

Run initialization in your target project root:

```bash
path-header-scanner init
```

This prepares required defaults/config artifacts used by the tool.

Optional flags:

- `--mode [config|templates|examples|all]`
- `--force`
- `--ask`

## 4) Run a dry-run scan first (recommended)

```bash
path-header-scanner scan app
```

No files are modified in dry-run mode.

## 5) Apply changes when output looks correct

```bash
path-header-scanner scan app --apply
```

## 6) Use help for any command

```bash
path-header-scanner --help
path-header-scanner init --help
path-header-scanner scan --help
```

## Suggested next steps

- Read command reference: `docs/user-guide/commands.md`
- Understand run/stop/remove lifecycle: `docs/user-guide/lifecycle.md`
- Tune configuration: `docs/configuration.md` (protected)
