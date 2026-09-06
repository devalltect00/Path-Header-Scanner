---
name: follow-path-header-scanner-guidelines
description: Apply Path Header Scanner-specific authorization, source layout, scan safety, environment, testing, and documentation rules.
---

# Follow Path Header Scanner Guidelines

## Purpose

Work safely and consistently in the Path Header Scanner repository. Apply this
skill together with the user's latest instruction and the repository's governing
files.

## Authorization and governing files

1. Treat the user's latest explicit instruction as the authority for the current
   task and write scope.
2. Read the repository-root `AGENTS.md` before source analysis or implementation.
3. Read `ENGINEERING_EXECUTION_POLICY.md` when architecture, implementation, CLI
   integration, or release readiness is relevant.
4. Use `pyproject.toml`, `Makefile`, configuration templates, and active source as
   executable truth.
5. Preserve unrelated work and obvious backup or temporary files.

Do not perform commits, tags, pushes, releases, package publication, registry
publication, or destructive cleanup without explicit approval.

## Project layout

- `app/cli/**`: commands, options, resolution, and presentation.
- `app/core/scan/**`: file discovery, validation, and path-header updates.
- `app/languages/**`: language-specific header strategies.
- `app/config/**`: configuration loading and precedence.
- `app/core/initialize/**`: generated configuration scaffolding.
- `app/ui/**` and `app/theme/**`: shared terminal presentation.
- `tests/**`: behavior and regression tests.
- `docs/**`: user, architecture, testing, and developer documentation.

Keep reusable scan behavior out of the CLI layer and keep language-specific
syntax inside language strategies.

## Scan safety contract

`path-header-scanner scan` is preview-only unless `--apply` is explicitly
provided. Read-only discovery and validation may execute in preview mode, but
source or documentation files must not be changed. Before validating live writes,
show the resolved target and prefer a dedicated test workspace.

Never use the application repository itself as an unintended scan target. Treat
`--workdir`, the positional target, configuration, and defaults according to the
active resolver implementation.

## Configuration and templates

The active user configuration is `.config/path_header_scanner/config.toml`; the
packaged default is `app/templates/config.toml`. When changing a field, update
the template, loader/resolver, tests, and relevant documentation together. Do
not unexpectedly overwrite generated user configuration.

## Environment and validation

Use the existing `venv/` when available. The package supports the Python range
declared in `pyproject.toml`; project containers and standard Make setup use
Python 3.14.

Run focused tests first, then broader checks. Use a repository-local
`--basetemp` on Windows when the system temporary directory has ACL problems.
Validate Make syntax, Compose configuration, and CLI `--help` for developer
workflow changes. Do not publish images during validation.

## Implementation and documentation

- Use type hints, useful docstrings, logging, and `pathlib` where practical.
- Keep functions focused and avoid duplicated or hardcoded path logic.
- Do not use debugging `print()` calls.
- Add proportionate tests for changed behavior.
- Update user and developer documentation for CLI, configuration, Make, Docker,
  initialization, scan, or output changes.
- Do not bump versions or edit changelog/release metadata unless requested.

## Completion report

Report what changed, files affected, validation results, documentation changes,
known limitations, anything skipped, and whether files were removed.
