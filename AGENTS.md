# AGENTS.md

## Project overview

Path Header Scanner is a configuration-driven Python CLI that discovers source
and documentation files, validates their path headers, previews missing or stale
headers, and applies approved corrections across supported languages.

The application is intended for both interactive development and repeatable
automation. Preserve deterministic path resolution, preview-first behavior,
language-aware syntax, clear summaries, and configuration compatibility.

## Supported user-facing commands

```text
path-header-scanner init
path-header-scanner scan <target>
```

`scan` is non-mutating by default. File updates require the explicit `--apply`
option. `--workdir` changes the base used to resolve a relative target, and
`--debug` enables detailed scan diagnostics.

## Technology and packaging

- Package compatibility: Python 3.11+
- Standard development and container runtime: Python 3.14
- Typer and Rich
- setuptools and setuptools-scm
- Ruff and Black
- Pytest and pytest-cov
- MkDocs Material
- Docker, Docker Compose, and modular Make helpers

The console entry point is defined in `pyproject.toml`. Package resources under
`app/templates/` must remain included in distributions.

## Project structure

```text
app/
├── cli/          CLI commands, arguments, resolution, and presentation
├── config/       Configuration loading and access
├── core/scan/    File discovery, validation, processing, and updates
├── languages/    Language-specific header strategies
├── models/       Shared result and enum models
├── services/     Application-level service composition
├── templates/    Configuration copied by init
├── theme/        Rich theme definitions
├── ui/           Shared terminal presentation
└── utils/        Path, parsing, logging, and environment utilities

tests/            Unit, integration, CLI, core, and service tests
docs/             User, architecture, testing, and developer documentation
make/             Modular local, Docker, Compose, and remote Make commands
```

The CLI entry point is `app/cli/main.py`. Keep parsing and presentation in
`app/cli/`, reusable scan behavior in `app/core/scan/`, and language syntax in
`app/languages/`.

## Scan safety contract

- Preview is the default and must not write target files.
- `--apply` is the only supported opt-in for scan mutations.
- Resolve the target and optional workdir before file discovery.
- Excluded directories such as `.git`, virtual environments, caches, and build
  outputs must remain excluded unless the user explicitly configures otherwise.
- Apply mode must update only files selected by the scanner and supported
  language strategies.
- Summaries should distinguish valid, inserted, updated, and failed files.

Use a temporary or dedicated testing project when validating apply mode. Never
scan or modify another repository merely because the command was invoked from
the Path Header Scanner source checkout.

## Dry-run contract

- `init --dry-run` must not create directories or files, overwrite content, or
  prompt for confirmation.
- `scan --dry-run` must remain non-mutating and must override `--apply` and a
  configured `apply = true` value.
- Read-only configuration loading, discovery, validation, and rendering may
  execute so the preview remains useful.
- Diagnostic logging may write to its configured destination, but target
  project files must remain unchanged.
- Every mutating command needs regression tests proving its dry-run boundary.

## Configuration and templates

Path Header Scanner uses `.config/path_header_scanner/config.toml`. The packaged
source template is `app/templates/config.toml`; generated target configuration
is user-owned after initialization.

When adding or changing a configuration field:

1. Update the packaged template and loader/resolver logic.
2. Preserve compatible defaults where practical.
3. Add tests for CLI/config/default precedence and validation.
4. Update command, configuration, QA, and architecture documentation as needed.

Never silently overwrite user-managed configuration.

## Coding and logging standards

- Follow PEP 8 and existing project conventions.
- Use type hints and useful docstrings.
- Prefer `pathlib` over `os.path`.
- Keep functions focused and responsibilities separated.
- Prefer composition and straightforward code over unnecessary abstraction.
- Do not change public CLI behavior without discussing compatibility.
- Preserve unrelated work and backup files in a dirty worktree.
- Do not use debugging `print()` calls or hardcoded project paths.

Use logging when it improves troubleshooting:

- `CRITICAL`: execution cannot continue safely.
- `ERROR`: an operation failed.
- `WARNING`: a recoverable issue or unsupported file was encountered.
- `INFO`: scan progress or an important state change.
- `DEBUG`: path resolution, strategy selection, or detailed flow.

Never log credentials or sensitive path contents unnecessarily.

## Testing and validation

Use the existing virtual environment when available:

```powershell
.\venv\Scripts\python.exe -m pytest
```

Run focused tests first and then the broader suite. On Windows, use a
repository-local `--basetemp` when the system temporary directory has ACL
problems. Scan changes require tests for both preview and `--apply` behavior.

Developer-workflow changes should validate:

- TOML parsing and metadata tests
- `make help` and representative Make dry-runs
- Docker Compose development and production configuration
- production and development CLI `--help` startup

Do not publish packages or images during ordinary validation.

## Documentation

Keep files under `docs/` synchronized with commands, supported languages,
configuration, initialization, scan behavior, output, Make targets, Docker
workflows, testing, and troubleshooting.

Significant architecture changes require an explanation of responsibilities,
dependencies, data flow, and trade-offs. Update Mermaid diagrams when they
materially improve understanding.

## Development workflow

1. Analyze the active implementation and configuration.
2. Describe affected files, compatibility, risks, and validation.
3. Implement focused changes.
4. Add or update tests and documentation.
5. Run focused and broader validation.

Before executing mutating scan, cleanup, publication, or release operations,
explain the target and obtain explicit approval.

## Git and release safeguards

Do not perform commits, tags, pushes, rebases, history rewrites, releases,
package publication, or registry publication unless explicitly requested and
approved. Do not edit `CHANGELOG.md` or bump the project version automatically.

## Completion report

Report:

1. What changed and why
2. Files added, modified, or removed
3. Tests and commands run, including results
4. Documentation changes or remaining work
5. Known limitations and the next recommended step
