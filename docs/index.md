<!-- docs/index.md -->

# Path Header Scanner Documentation

Welcome to the official documentation for **Path Header Scanner**.

This documentation is organized for multiple audiences:

- **Users**: install, initialize, run, and operate the tool
- **Developers**: understand codebase structure, workflows, and contribution practices
- **Architects/Maintainers**: review internals, component responsibilities, and execution flow
- **Readers/Learners**: supporting notes and references

---

## Documentation Entry Points

## User Documentation

- [User Guide Overview](user-guide/overview.md)
- [Quick Start](user-guide/quickstart.md)
- [Commands Reference](user-guide/commands.md)
- [Installation Methods](user-guide/installation-methods.md)
- [Lifecycle (Start/Run/Stop/Remove)](user-guide/lifecycle.md)

## Developer Documentation

- [Developer Getting Started](developer-guide/getting-started.md)
- [Developer Guide](developer-guide/developer-guide.md)
- [Docker Workflow](developer-guide/docker-workflow.md)
- [AI Development Workflow](developer-guide/blackbox/ai-development-workflow.md)
- [Ruff Ignore Rules](developer-guide/tooling/ruff/ruff-ignore.md)
- [Ruff Select Rules](developer-guide/tooling/ruff/ruff-select.md)

## Architecture Documentation

- [Architecture Design Patterns](architecture/design-patterns.md)
- [Architecture Workflow](architecture/workflow.md)
- [Architecture Diagrams](architecture/diagrams.md)

## Project and Testing Documentation

- [Project Structure](project/project-structure.md)
- [Supported Languages](project/languages/supported-languages.md)
- [Markdown Language Strategy](project/languages/markdown-language-strategy.md)
- [Testing Guide](testing/testing-guide.md)

## Reads and Notes

- [Documentation Audit Report](reads/documentation-audit-report.md)
- [Linting vs Formatting](reads/linting-vs-formatting.md)
- [Ruff Notes](reads/ruff.md)

---

## Protected Core Docs (Reference Only)

The following files are protected and intentionally preserved:

- `docs/badges.md`
- `docs/configuration.md`
- `docs/infrastructure.md`
- `docs/installation.md`
- `docs/usage.md`

---

## Tool Scope Summary

Path Header Scanner is a CLI utility that:

- scans project files recursively
- validates and normalizes path headers
- inserts missing headers or updates invalid ones
- supports multiple language strategies
- preserves special lines where required (for example shebang and `<?php` handling)

Primary CLI entrypoint:

- `app/cli/main.py`

Core commands:

- `init`
- `scan`
