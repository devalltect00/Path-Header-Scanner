# ENGINEERING_EXECUTION_POLICY.md

## Goal

Deliver a predictable, maintainable, and safe path-header scanning CLI.

## Architecture responsibilities

| Layer | Responsibility |
| --- | --- |
| CLI | Parse arguments, coordinate interaction, and present results |
| Config | Load configuration and resolve CLI/config/default precedence |
| Scanner | Discover supported files without mutating them |
| Processor | Validate headers and coordinate preview or approved updates |
| Languages | Define language-specific header parsing and rendering |
| Initialize | Generate project configuration resources |
| UI | Provide shared Rich presentation |

Do not place filesystem mutation or language syntax rules in the CLI layer.

## Safety requirements

- Scan preview is non-mutating by default.
- File writes require explicit `--apply` selection.
- Resolve and log the target before processing.
- Never modify excluded, unsupported, or undiscovered files.
- Never expose credentials or sensitive file contents in logs.

## Quality requirements

- Type hints and useful docstrings
- Focused functions and clear layer boundaries
- Logging instead of debugging `print()` calls
- Tests for preview and apply behavior
- Synchronized CLI, configuration, and developer documentation

## Release readiness

- CLI startup and help succeed locally and in production containers.
- Tests and static checks complete with known failures documented.
- Make and Compose workflows parse correctly.
- No debug code, unreviewed generated files, or unintended mutations remain.

Prefer simple, predictable, and maintainable solutions over clever ones.
