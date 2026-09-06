# Configuration

This document describes how Path Header Scanner can be configured.

## Overview

Path Header Scanner works out of the box with sensible defaults and typically requires little or no configuration.

Configuration may be provided through:

- Command-line options
- Configuration files
- Environment variables (if supported)
- Future extensions

---

## Default Behavior

By default, Path Header Scanner:

- Scans supported files
- Detects path headers
- Reports findings
- Does not modify files unless explicitly instructed

Example:

```bash
path-header-scanner scan .
```

---

## Command-Line Configuration

Most configuration is provided through command-line options.

### Apply Changes

```bash
path-header-scanner scan . --apply
```

Apply detected updates directly to files.

---

### Debug Mode

```bash
path-header-scanner scan . --debug
```

Display additional diagnostic information.

### Dry-run Mode

```bash
path-header-scanner init --dry-run
path-header-scanner scan . --apply --dry-run
```

Dry-run prevents initialization and scan writes. It overrides `--apply`.

---

## Configuration File

### File location

Path Header Scanner reads `.config/path_header_scanner/config.toml`.

```toml
[tool.path-header-scanner.cli.execution]
dry_run = false
debug = false

[tool.path-header-scanner.cli.scan]
apply = false
```

---

## Proposed Configuration Structure

Example:

```toml
[scanner]
recursive = true
follow_symlinks = false

[headers]
enabled = true
auto_update = false

[output]
verbose = false
color = true
```

---

## File Discovery

Future versions may automatically search for configuration files in:

```text
project-root/
├── path-header-scanner.toml
├── config.toml
└── pyproject.toml
```

Priority:

```text
CLI Options
    ↓
Project Configuration (`.config/path_header_scanner/config.toml`)
    ↓
Default Settings
```

---

## Environment Variables

Future versions may support environment variables.

Example:

```bash
PATH_HEADER_SCANNER_DEBUG=true
```

```bash
PATH_HEADER_SCANNER_COLOR=false
```

---

## Configuration Priority

When multiple configuration sources exist, the following priority should apply:

```text
Command Line Arguments
    ↓
Environment Variables
    ↓
Configuration File
    ↓
Built-in Defaults
```

---

## Best Practices

### Use Version Control

Store project configuration files in version control.

Example:

```text
path-header-scanner.toml
```

### Keep Configuration Minimal

Only override settings when necessary.

### Prefer Project-Level Configuration

Avoid machine-specific settings whenever possible.

---

## Future Enhancements

Potential future configuration options:

- Custom header formats
- Additional file types
- Ignore patterns
- Output formatting
- Reporting configuration
- Plugin support
- Validation rules

---

## Related Documentation

- Installation Guide
- Usage Guide
- Project Structure Guide
- Development Guide
- Infrastructure Guide
