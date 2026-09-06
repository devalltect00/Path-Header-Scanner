<!-- docs/path-header/README.md -->

# Path Header Scanner

Path Header Scanner is a developer utility used to automatically:

- insert missing path headers
- validate existing headers
- replace invalid headers
- normalize relative file path visibility

The project is designed for:

- local development
- Docker workflows
- CI/CD pipelines
- multi-language repositories

---

# Example

Example generated header:

```python
# app/core/scanner.py
```

Example source file:

```python
# app/core/scanner.py

class FileScanner:
    ...
```

---

# Features

# Core Features

- recursive directory scanning
- automatic header generation
- missing header insertion
- invalid header replacement
- dry-run support
- debug logging
- Docker support
- Docker Compose support
- Makefile integration
- mounted workspace support

---

# Language Features

- multi-language support
- language strategy architecture
- shebang preservation
- encoding declaration preservation
- PHP opening tag preservation
- safe insertion handling

---

# Developer Features

- modular architecture
- strategy pattern implementation
- structured logging
- pathlib-based filesystem handling
- extensible language system
- CI/CD friendly execution

---

# Supported Languages

| Language | Extensions |
|---|---|
| Python | `.py` |
| JavaScript | `.js` |
| React | `.jsx` |
| TypeScript | `.ts`, `.tsx` |
| Shell | `.sh`, `.bash`, `.zsh` |
| PHP | `.php` |
| HTML | `.html`, `.htm` |

---

# Before and After

# Python

Before:

```python
print("hello")
```

After:

```python
# app/main.py

print("hello")
```

---

# JavaScript

Before:

```javascript
console.log("hello")
```

After:

```javascript
// app/main.js

console.log("hello")
```

---

# HTML

Before:

```html
<html>
</html>
```

After:

```html
<!-- app/templates/index.html -->

<html>
</html>
```

---

# Installation

# Local Installation

Install editable development environment:

```bash
pip install -e .[dev]
```

Run CLI:

```bash
py -m app --help
```

---

# Docker Installation

Build image:

```bash
docker build -t path-header-scanner .
```

or:

```bash
docker compose build
```

---

# Quick Start

# Dry Run

```bash
path-header-scanner scan app
```

or:

```bash
py -m app scan app
```

---

# Apply Changes

```bash
path-header-scanner scan app --apply
```

---

# Debug Mode

```bash
path-header-scanner scan app --debug
```

---

# Docker Usage

## Windows CMD

```cmd
docker run -it --rm -w /workspace -v "%cd%:/workspace" path-header-scanner scan app
```

## PowerShell / Linux / macOS

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app
```

---

# Docker Apply Changes

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app --apply
```

---

# Makefile Usage

# Build Image

```bash
make docker-build
```

---

# Dry Run

```bash
make docker-scan
```

---

# Apply Changes

```bash
make docker-apply
```

---

# Debug Mode

```bash
make docker-debug
```

---

# Include / Exclude Target Directory

The scanner supports configurable header generation.

---

# Include Target Directory

Default behavior:

```python
# app/cli/main.py
```

Example:

```bash
path-header-scanner scan app \
    --include-target-directory
```

---

# Exclude Target Directory

Example:

```python
# cli/main.py
```

Command:

```bash
path-header-scanner scan app \
    --exclude-target-directory
```

---

# Command Overview

Main command:

```bash
path-header-scanner scan TARGET_DIRECTORY
```

---

# Common Options

| Option | Description |
|---|---|
| `--apply` | Write changes to files |
| `--debug` | Enable debug logging |
| `--workdir` | Custom working directory |
| `--include-target-directory` | Include scan target in headers |
| `--exclude-target-directory` | Exclude scan target from headers |

---

# Project Structure

```text
app/
├── cli/
├── constants/
├── core/
├── languages/
├── models/
├── utils/
└── __main__.py
```

See full structure in [`project_structure.md`](../project/project-structure.md).

---

# Architecture Overview

The project is organized into layers.

| Layer | Responsibility |
|---|---|
| CLI | User commands |
| Core | Processing orchestration |
| Languages | Language-specific logic |
| Models | Shared data structures |
| Utils | Shared helpers |
| Constants | Global constants |

---

# Processing Flow

```text
scan files
↓
resolve strategy
↓
extract header
↓
validate header
↓
insert/update if needed
↓
collect results
↓
display summary
```

---

# Output Example

```text
Scanning directory: app

Found 25 supported files

~ app/utils/helper.py (updated)
+ app/core/main.py (inserted)

SUMMARY

Valid: 22
Updated: 1
Inserted: 1
Failed: 0
```

---

# Ignored Directories

Ignored by default:

- `.git`
- `.venv`
- `venv`
- `__pycache__`
- `node_modules`
- `dist`
- `build`

---

# Documentation

| Document | Description |
|---|---|
| `user_guide.md` | End-user usage guide |
| `developer_guide.md` | Internal architecture guide |
| `docker.md` | Docker workflow documentation |
| `workflow.md` | Processing workflow explanation |
| `diagrams.md` | Mermaid architecture diagrams |

---

# Recommended Workflow

# Step 1

Run dry-run scan:

```bash
path-header-scanner scan app
```

---

# Step 2

Review output.

---

# Step 3

Apply changes:

```bash
path-header-scanner scan app --apply
```

---

# Step 4

Commit updated files.

---

# Why Use Path Header Scanner?

Benefits:

- easier source navigation
- clearer file visibility
- consistent repository structure
- improved debugging context
- maintainable code organization
- automated path normalization

---

# Future Improvements

Potential future enhancements:

- TOML configuration
- custom templates
- progress bars
- parallel processing
- plugin system
- Git hook integration
- pre-commit support
- configurable ignored directories

---

# License

See:

```text
LICENSE
```

---

# Notes

- Paths use POSIX separators.
- Docker workflows support mounted workspaces.
- Existing special lines are preserved safely.
- File updates preserve trailing newlines.
- Relative path generation is configurable.
