<!-- docs/path-header/workflow.md -->

# Processing Workflow

This document explains the internal processing workflow of Path Header Scanner.

It describes:

- execution stages
- path resolution
- language strategy resolution
- header validation
- file updates
- result aggregation
- logging flow

---

# High-Level Workflow

```text
parse CLI arguments
↓
resolve target path
↓
scan source files
↓
resolve language strategy
↓
extract existing header
↓
generate expected header
↓
validate header
↓
insert/update if needed
↓
collect processing results
↓
display summary
```

---

# Full Processing Flow

```text
CLI Command
↓
Typer Argument Parsing
↓
Path Resolution
↓
File Scanning
↓
Language Strategy Resolution
↓
File Processing
↓
Header Validation
↓
File Update (optional)
↓
Result Aggregation
↓
Summary Reporting
```

---

# Stage 1 — CLI Parsing

The workflow begins from:

```python
app/cli/main.py
```

The CLI is implemented using:

- Typer
- pathlib
- structured logging

Main command:

```bash
path-header-scanner scan TARGET_DIRECTORY
```

---

# CLI Responsibilities

The CLI layer is responsible for:

- parsing arguments
- parsing options
- initializing strategies
- resolving paths
- creating scanner and processor instances
- displaying summaries

---

# Supported CLI Options

| Option | Purpose |
|---|---|
| `--apply` | Write file changes |
| `--debug` | Enable debug logging |
| `--workdir` | Custom working directory |
| `--include-target-directory` | Include scan target in headers |
| `--exclude-target-directory` | Exclude scan target from headers |

---

# Stage 2 — Path Resolution

The target directory is resolved using:

```python
resolve_target_path()
```

Responsibilities:

- normalize paths
- support Docker workspaces
- support custom workdirs
- resolve relative paths safely

---

# Path Resolution Order

Resolution priority:

```text
absolute path
↓
working directory
↓
current working directory
↓
Docker workspace
↓
direct relative path
```

---

# Example

Input:

```bash
scan app
```

Docker runtime:

```bash
-w /workspace
```

Resolved path:

```text
/workspace/app
```

---

# Stage 3 — Scanner Initialization

The CLI initializes:

```python
FileScanner
```

with:

- resolved root directory
- language strategies
- ignored directories

---

# Scanner Responsibilities

The scanner:

- recursively walks directories
- skips ignored directories
- filters supported extensions
- returns matching source files

---

# Ignored Directories

Ignored by default:

```text
.git
.venv
venv
__pycache__
node_modules
dist
build
```

---

# Recursive Scanning

Scanning uses:

```python
Path.rglob("*")
```

Workflow:

```text
walk directories
↓
skip ignored paths
↓
check supported extensions
↓
collect matching files
↓
sort files
↓
return file list
```

---

# Stage 4 — Strategy Resolution

Each file is matched against a language strategy.

Example:

```text
main.py
↓
PythonLanguageStrategy
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

Strategies define:

- supported extensions
- comment syntax
- header extraction
- insertion handling
- special-line preservation

---

# Stage 5 — File Processing

Each discovered file is processed individually.

Workflow:

```text
read file
↓
split into lines
↓
extract current header
↓
generate expected header
↓
compare headers
↓
insert/update if needed
↓
return processing result
```

---

# Stage 6 — Header Extraction

Each strategy determines whether a file already contains a header.

Examples:

Python:

```python
# app/main.py
```

JavaScript:

```javascript
// app/main.js
```

HTML:

```html
<!-- app/index.html -->
```

---

# Special-Line Preservation

Some languages require preserving special lines.

---

# Python

Preserved:

- shebang lines
- encoding declarations

Example:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# app/main.py
```

---

# PHP

Preserved:

- shebangs
- `<?php`

Example:

```php
<?php
// app/index.php
```

---

# Shell

Preserved:

- shebang lines

Example:

```bash
#!/bin/bash
# scripts/build.sh
```

---

# Stage 7 — Expected Header Generation

Expected headers are generated using:

```python
build_header()
```

based on relative file paths.

---

# Include Target Directory

Default behavior:

```python
# app/cli/main.py
```

Enabled using:

```bash
--include-target-directory
```

---

# Exclude Target Directory

Alternative behavior:

```python
# cli/main.py
```

Enabled using:

```bash
--exclude-target-directory
```

---

# Header Generation Flow

```text
resolve relative path
↓
apply include/exclude logic
↓
convert to POSIX path
↓
prepend comment syntax
↓
return formatted header
```

---

# Stage 8 — Validation

The current header is compared against the expected header.

Possible outcomes:

| State | Meaning |
|---|---|
| VALID | Header already correct |
| UPDATED | Existing header replaced |
| INSERTED | Missing header inserted |
| FAILED | Processing error occurred |

---

# Validation Logic

```text
extract current header
↓
compare with expected header
↓
determine result state
```

---

# VALID State

Example:

```python
# app/main.py
```

already matches expected output.

No update required.

---

# UPDATED State

Example:

Before:

```python
# old/path.py
```

After:

```python
# app/main.py
```

---

# INSERTED State

Example:

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

# FAILED State

Failures may occur due to:

- encoding issues
- permissions
- invalid filesystem state
- unexpected exceptions

Failures are captured safely using:

```python
try/except
```

---

# Stage 9 — File Updates

Updates are only written when:

```bash
--apply
```

is enabled.

---

# Dry Run Mode

Default behavior:

```bash
path-header-scanner scan app
```

No files modified.

---

# Apply Mode

```bash
path-header-scanner scan app --apply
```

Files updated on disk.

---

# File Rebuilding

The updater safely rebuilds file content:

```text
preserve special lines
↓
insert/replace header
↓
preserve remaining content
↓
normalize trailing newline
```

---

# Stage 10 — Result Aggregation

Each processed file returns:

```python
FileProcessResult
```

containing:

- file path
- status
- expected header
- current header
- messages

---

# Summary Generation

The processor aggregates results:

```text
VALID
UPDATED
INSERTED
FAILED
```

and generates final statistics.

---

# Example Summary

```text
SUMMARY

Valid: 22
Updated: 1
Inserted: 1
Failed: 0
```

---

# Logging Workflow

The project uses structured logging.

---

# Recommended Logging Levels

| Level | Purpose |
|---|---|
| DEBUG | detailed processing |
| INFO | summaries and updates |
| WARNING | recoverable issues |
| ERROR | failures |

---

# Recommended Output Behavior

| Status | Logging Level |
|---|---|
| VALID | DEBUG |
| UPDATED | INFO |
| INSERTED | INFO |
| FAILED | ERROR |

---

# Docker Workflow

Typical Docker execution:

```text
build image
↓
mount workspace
↓
set working directory
↓
run scanner
↓
modify mounted files
↓
remove container
```

---

# Docker Path Flow

Example:

```bash
docker run -it --rm \
    -w /workspace \
    -v "${PWD}:/workspace" \
    path-header-scanner \
    scan app
```

Path resolution:

```text
host project
↓
mounted to /workspace
↓
scan app
↓
resolved to /workspace/app
```

---

# Makefile Workflow

Example:

```bash
make docker-debug
```

expands internally to:

```bash
docker run -it --rm \
    -w /workspace \
    -v "$(CURDIR):/workspace" \
    path-header-scanner \
    scan app --debug
```

---

# Error Handling Workflow

Errors are isolated per file.

Workflow:

```text
process file
↓
exception raised
↓
log exception
↓
return FAILED result
↓
continue processing remaining files
```

This prevents a single failure from stopping the full scan.

---

# Scalability Considerations

Recommended practices for large repositories:

- use INFO summaries only
- log VALID files in DEBUG mode
- avoid excessive console output
- use mounted workspaces
- prefer dry-run before apply

---

# Future Workflow Enhancements

Potential future improvements:

- parallel processing
- progress bars
- configuration files
- incremental scanning
- cache support
- Git integration
- pre-commit hooks
- plugin system

---

# Notes

- File processing is deterministic.
- Relative paths use POSIX separators.
- File updates preserve trailing newlines.
- Language strategies remain isolated and reusable.
- Docker workflows are optimized for mounted workspace development.
