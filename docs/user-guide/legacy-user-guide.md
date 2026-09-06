<!-- docs/path-header/user_guide.md -->

# docs/path-header/user_guide.md

# User Guide

This document explains how to use Path Header Scanner.

---

# Overview

Path Header Scanner is a CLI utility used to:

- scan source files recursively
- validate path headers
- insert missing headers
- update invalid headers
- preserve language-specific special lines

Supported environments:

- local Python execution
- Docker
- Docker Compose
- CI/CD pipelines

---

# Installation

# Local Python Installation

Install in editable mode:

```bash
pip install -e .[dev]
```

Run:

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

# CLI Overview

Main command:

```bash
path-header-scanner scan [TARGET_DIRECTORY]
```

or:

```bash
py -m app scan [TARGET_DIRECTORY]
```

---

# Command Structure

```bash
path-header-scanner scan TARGET_DIRECTORY [OPTIONS]
```

---

# Arguments

## TARGET_DIRECTORY

Directory to scan recursively.

Examples:

```bash
path-header-scanner scan app
```

```bash
path-header-scanner scan src
```

```bash
path-header-scanner scan .
```

---

# Options

## --apply

Write file modifications to disk.

Without `--apply`, the scanner runs in dry-run mode.

Example:

```bash
path-header-scanner scan app --apply
```

---

## --debug

Enable debug logging.

Shows:
- detailed path resolution
- processed files
- internal diagnostics

Example:

```bash
path-header-scanner scan app --debug
```

---

## --workdir

Specify a custom working directory used to resolve relative paths.

Useful for:
- Docker
- mounted volumes
- CI environments
- monorepos

Example:

```bash
path-header-scanner scan src --workdir /workspace/project
```

---

## --include-target-directory

Include the target directory in generated headers.

Default:

```text
# app/cli/main.py
```

Example:

```bash
path-header-scanner scan app --include-target-directory
```

---

## --exclude-target-directory

Exclude the target directory from generated headers.

Example:

```text
# cli/main.py
```

Example command:

```bash
path-header-scanner scan app --exclude-target-directory
```

---

# Common Usage Examples

# Dry Run

Scan files without modifying them.

```bash
path-header-scanner scan app
```

Python module:

```bash
py -m app scan app
```

---

# Apply Changes

Update files directly.

```bash
path-header-scanner scan app --apply
```

---

# Debug Mode

Enable verbose logging.

```bash
path-header-scanner scan app --debug
```

---

# Scan Current Directory

```bash
path-header-scanner scan .
```

---

# Exclude Target Directory From Headers

```bash
path-header-scanner scan app --exclude-target-directory
```

Result:

```python
# cli/main.py
```

---

# Include Target Directory In Headers

```bash
path-header-scanner scan app --include-target-directory
```

Result:

```python
# app/cli/main.py
```

---

# Docker Usage

# Build Docker Image

```bash
docker build -t path-header-scanner .
```

or:

```bash
docker compose build
```

---

# Docker Dry Run

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

# Docker Apply Changes

## Windows CMD

```cmd
docker run -it --rm -w /workspace -v "%cd%:/workspace" path-header-scanner scan app --apply
```

## PowerShell

```powershell
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app --apply
```

---

# Docker Debug Mode

```bash
docker run -it --rm -w /workspace -v "${PWD}:/workspace" path-header-scanner scan app --debug
```

---

# Docker Compose Usage

# Dry Run

```bash
docker compose run --rm path-header-scanner scan app
```

---

# Apply Changes

```bash
docker compose run --rm path-header-scanner scan app --apply
```

---

# Debug Mode

```bash
docker compose run --rm path-header-scanner scan app --debug
```

---

# Makefile Usage

# Build

```bash
make docker-build
```

---

# Scan

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

# Custom Target

```bash
make docker-debug TARGET=src
```

---

# Header Examples

# Python

```python
# app/main.py
```

---

# JavaScript

```javascript
// app/main.js
```

---

# HTML

```html
<!-- app/templates/index.html -->
```

---

# PHP

```php
<?php
// app/index.php
```

---

# Shell

```bash
#!/bin/bash
# scripts/build.sh
```

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

# Processing Behavior

The scanner:

- scans directories recursively
- skips ignored directories
- preserves special language lines
- updates invalid headers safely
- inserts missing headers automatically

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

# Preserved Special Lines

# Python

Preserved:
- shebangs
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
- `<?php` opening tags

---

# Shell

Preserved:
- shebang lines

---

# Output Example

```text
Scanning directory: app

Found 25 supported files

~ app/utils/helper.py (updated)
+ app/core/main.py (inserted)
x app/broken/file.py (failed)

SUMMARY

Valid: 22
Updated: 1
Inserted: 1
Failed: 1
```

---

# Status Meanings

| Status | Meaning |
|---|---|
| valid | Header already correct |
| updated | Invalid header replaced |
| inserted | Missing header inserted |
| failed | Processing failed |

---

# Exit Behavior

| Exit Code | Meaning |
|---|---|
| 0 | Success |
| 1 | Failure |

---

# Recommended Workflow

Recommended workflow for teams:

## Step 1

Run dry-run scan:

```bash
path-header-scanner scan app
```

## Step 2

Review output.

## Step 3

Apply changes:

```bash
path-header-scanner scan app --apply
```

## Step 4

Commit updated files.

---

# CI/CD Example

Example GitHub Actions usage:

```yaml
- name: Run Path Header Scanner
  run: |
    docker run --rm \
      -w /workspace \
      -v "${PWD}:/workspace" \
      path-header-scanner \
      scan app
```

---

# Notes

- Paths use POSIX-style separators.
- Files are processed recursively.
- Existing headers are updated safely.
- Existing special lines are preserved.
- Docker support works with mounted workspaces.
- Relative paths are normalized automatically.
