<!-- docs/developer-guide/getting-started.md -->

# Developer Getting Started

This guide helps developers start working on Path Header Scanner quickly and safely.

## 1) Clone and enter repository

```bash
git clone https://github.com/devalltect00/Path-Header-Scanner.git
cd Path-Header-Scanner
```

## 2) Create environment and install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

## 3) Validate local setup

```bash
path-header-scanner --help
py -m app --help
```

## 4) Run initialization and sample scan

```bash
path-header-scanner init
path-header-scanner scan app
```

## 5) Run tests and lint checks

```bash
pytest -v
ruff check app tests
ruff format app tests
```

## 6) Main code map

- CLI entrypoint: `app/cli/main.py`
- Init command: `app/cli/commands/init/command.py`
- Scan command: `app/cli/commands/scan/command.py`
- Core scan engine: `app/core/scan/`
- Initialization core: `app/core/initialize/`
- Language strategies: `app/languages/`
- Tests: `tests/`

## 7) Development safety checklist

- Run dry-run before apply operations
- Keep docs aligned with real code behavior
- Confirm tests pass before finalizing
- Avoid changing protected docs unless explicitly requested
