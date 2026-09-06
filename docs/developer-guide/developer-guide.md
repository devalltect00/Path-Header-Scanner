<!-- docs/path-header/developer_guide.md -->

# Developer Guide

This document explains the internal architecture, development workflow, and implementation details of Path Header Scanner.

---

# Overview

Path Header Scanner is designed as a modular and extensible CLI utility for:

- recursive source file scanning
- path header validation
- missing header insertion
- invalid header replacement
- multi-language support
- Docker-based execution

The architecture emphasizes:

- separation of concerns
- strategy-based language handling
- safe file updates
- reusable utilities
- maintainable CLI tooling

---

# Architecture Overview

The project is divided into multiple layers.

| Layer | Responsibility |
|---|---|
| CLI | User commands and argument parsing |
| Core | Processing orchestration |
| Languages | Language-specific behaviors |
| Models | Shared result models and enums |
| Utils | Shared helpers and utilities |
| Constants | Global constants and configuration |

---

# Project Structure

See full structure in [`project_structure.md`](../project/project-structure.md).

---

# Core Components

# FileScanner

Responsible for:

- recursive directory scanning
- ignored directory filtering
- supported extension filtering
- returning discovered source files

Main responsibilities:

```python
scanner.scan()
```

Features:

- recursive scanning using `Path.rglob()`
- ignored directory support
- extension-based matching
- sorted file output

---

# FileProcessor

Central orchestration layer.

Responsible for:

- strategy resolution
- file processing delegation
- result aggregation
- logging and summaries

Main responsibilities:

```python
processor.process_files()
```

Features:

- strategy lookup
- updater delegation
- centralized reporting
- result collection

---

# FileUpdater

Responsible for:

- safe file updates
- header insertion
- invalid header replacement
- preserving special lines

Main responsibilities:

```python
updater.process_file()
```

Features:

- shebang preservation
- encoding preservation
- PHP opening tag preservation
- newline-safe rebuilding

---

# Path Resolution

Path resolution is handled by:

```python
resolve_target_path()
```

Features:

- absolute path support
- Docker workspace fallback
- custom working directory support
- normalized path resolution

Resolution order:

1. absolute path
2. working directory
3. current working directory
4. Docker workspace
5. direct relative path

---

# Language Strategy System

The project uses the Strategy Pattern.

Each language implementation defines:

- supported extensions
- comment syntax
- insertion behavior
- header extraction logic

Base interface:

```python
class BaseLanguageStrategy(ABC):
```

---

# Supported Strategies

| Strategy | Extensions |
|---|---|
| PythonLanguageStrategy | `.py` |
| JavaScriptLanguageStrategy | `.js`, `.jsx`, `.ts`, `.tsx` |
| ShellLanguageStrategy | `.sh`, `.bash`, `.zsh` |
| PhpLanguageStrategy | `.php` |
| HtmlLanguageStrategy | `.html`, `.htm` |
| MarkdownLanguageStrategy | `.md`, `.markdown` |

---

# Strategy Responsibilities

Each strategy can implement:

| Method | Required | Purpose |
|---|---|---|
| `extensions` | Yes | Supported extensions |
| `comment_prefix` | Yes | Header comment syntax |
| `extract_header()` | Yes | Detect existing headers |
| `get_insertion_index()` | Optional | Preserve special lines |
| `build_header()` | Optional | Custom header formatting |

---

# Example Strategy

```python
class PythonLanguageStrategy(
    BaseLanguageStrategy
):
```

Features:

- Python comment syntax
- shebang preservation
- encoding declaration preservation

---

# Adding New Languages

Example:

```python
class RustLanguageStrategy(
    BaseLanguageStrategy
):
```

Required:

```python
@property
def extensions(self) -> list[str]:
```

```python
@property
def comment_prefix(self) -> str:
```

```python
def extract_header(
    self,
    lines: list[str],
) -> Optional[str]:
```

Optional:

```python
def get_insertion_index(
    self,
    lines: list[str],
) -> int:
```

---

# Header Generation

Headers are generated from relative paths.

Example:

```python
# app/core/scanner.py
```

The scanner supports:

- including target directory
- excluding target directory

Examples:

Included:

```python
# app/cli/main.py
```

Excluded:

```python
# cli/main.py
```

Controlled via:

```bash
--include-target-directory
```

or:

```bash
--exclude-target-directory
```

---

# Processing Flow

High-level workflow:

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

# Logging Design

The project uses structured logging.

Recommended levels:

| Level | Purpose |
|---|---|
| INFO | summaries and updates |
| DEBUG | detailed diagnostics |
| WARNING | recoverable issues |
| ERROR | failures |

Examples:

INFO:

```text
Updated: app/core/main.py
```

DEBUG:

```text
Processing: app/core/scanner.py
```

---

# Docker Support

The project supports:

- direct Docker execution
- Docker Compose
- mounted workspace development

Example:

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app
```

---

# Makefile Integration

The project includes Makefile helpers.

Examples:

```bash
make docker-build
```

```bash
make docker-scan
```

```bash
make docker-apply
```

```bash
make docker-debug
```

---

# Development Workflow

# Install Dependencies

```bash
pip install -e .[dev]
```

---

# Run Tests

```bash
pytest
```

---

# Run Coverage

```bash
pytest --cov=app
```

---

# Run Linting

```bash
ruff check .
```

---

# Format Code

```bash
ruff format .
```

---

# Run Scanner

```bash
py -m app scan app
```

---

# Apply Changes

```bash
py -m app scan app --apply
```

---

# Debug Mode

```bash
py -m app scan app --debug
```

---

# Docker Development

Build image:

```bash
docker compose build
```

Run scanner:

```bash
docker compose run --rm \
    path-header-scanner \
    scan app
```

Open shell:

```bash
docker compose run --rm \
    path-header-scanner \
    bash
```

---

# Design Principles

The project follows several design principles.

---

# Separation of Concerns

Each layer has a focused responsibility.

Examples:

- scanner only scans
- updater only updates
- strategies only define language behavior

---

# Composition Over Inheritance

Strategies are composed into processors instead of tightly coupled inheritance chains.

---

# Pathlib Usage

The project consistently uses:

```python
pathlib.Path
```

instead of:

```python
os.path
```

Benefits:

- cleaner APIs
- cross-platform compatibility
- easier path manipulation

---

# Structured Logging

The project avoids:

```python
print()
```

in favor of:

```python
logger.info()
```

Benefits:

- configurable verbosity
- CI/CD friendliness
- debug support

---

# Safe File Updates

File rebuilding preserves:

- shebangs
- encoding declarations
- PHP opening tags
- line ordering

---

# Documentation Rules

Every:

- module
- class
- method
- public function

must contain docstrings.

Preferred style:

- descriptive summaries
- typed arguments
- examples where appropriate

---

# Testing Recommendations

Recommended testing layers:

| Test Type | Purpose |
|---|---|
| Unit Tests | strategies and utilities |
| Integration Tests | processing workflow |
| CLI Tests | Typer command behavior |
| Docker Tests | container execution |

---

# Recommended Future Improvements

Potential future enhancements:

- configurable ignored directories
- `.path-header-ignore`
- custom header templates
- progress bars
- parallel processing
- TOML configuration support
- pre-commit integration
- CI validation mode
- Git hooks

---

# Notes

- All paths use POSIX separators in headers.
- File updates preserve trailing newlines.
- Logging is centralized through the processor layer.
- Docker support is designed for mounted workspace development.
- Strategies should remain lightweight and isolated.
