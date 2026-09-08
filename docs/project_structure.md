# Project Structure

# Repository Overview

This repository follows a modular structure commonly used in modern projects.

Common directories include:

- `app/` — Main application source code.
- `.config/` — Project configuration files.
- `.github/` — GitHub-related configuration.
- `.vscode/` — Visual Studio Code workspace settings.
- `docs/` — Project documentation and technical references.
- `tests/` — Automated tests.
- `data/` — Input datasets or static data.
- `output/` — Generated outputs from the application.
- `scripts/` — Utility scripts for development or automation.
- `tools/` — Development tools and automation utilities.
- `templates/` — Reusable templates used by the project.

---

# Repository Structure

(project type: ProjectType.PYTHON)

```text
.
├── .agents
│   └── skills
│       └── follow-path-header-scanner-guidelines
│           └── SKILL.md
├── .config
│   ├── custy
│   │   ├── templates
│   │   │   ├── backups
│   │   │   │   ├── commit
│   │   │   │   └── tag
│   │   │   ├── changelog
│   │   │   │   └── changelog.j2
│   │   │   ├── examples
│   │   │   │   ├── commit_message
│   │   │   │   └── tag_message
│   │   │   ├── commit-message.txt
│   │   │   └── tag-message.txt
│   │   └── config.toml
│   ├── doc_gen
│   │   └── config.toml
│   ├── path_header_scanner
│   │   └── config.toml
│   └── reflow
│       └── config.toml
├── .gitlab
│   ├── ci.yml
│   ├── docker-dev.yml
│   ├── docker-prod.yml
│   ├── python-package.yml
│   └── release.yml
├── .ruff_cache/ ... (collapsed)
├── app
│   ├── cli
│   │   ├── commands
│   │   │   ├── init
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   ├── main
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   ├── scan
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   └── __init__.py
│   │   ├── constants
│   │   │   ├── args.py
│   │   │   ├── completions.py
│   │   │   └── enums.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   └── versions.py
│   │   ├── errors.py
│   │   └── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config_loader.py
│   ├── constants
│   │   ├── docker.py
│   │   └── path.py
│   ├── core
│   │   ├── build/ ... (collapsed)
│   │   ├── initialize
│   │   │   ├── builder
│   │   │   │   └── init_builder.py
│   │   │   ├── models
│   │   │   │   ├── init_config.py
│   │   │   │   ├── init_spec.py
│   │   │   │   ├── initialization_result.py
│   │   │   │   ├── template_dir.py
│   │   │   │   └── template_file.py
│   │   │   ├── presenters
│   │   │   │   └── initialization_presenter.py
│   │   │   ├── services
│   │   │   │   └── scaffold_generator.py
│   │   │   ├── loader.py
│   │   │   ├── main.py
│   │   │   └── registry.py
│   │   ├── scan
│   │   │   ├── processor.py
│   │   │   ├── scanner.py
│   │   │   └── updater.py
│   │   └── shared
│   │       ├── __init__.py
│   │       ├── exceptions.py
│   │       └── result.py
│   ├── languages
│   │   ├── base.py
│   │   ├── html.py
│   │   ├── javascript.py
│   │   ├── markdown.py
│   │   ├── php.py
│   │   ├── python.py
│   │   └── shell.py
│   ├── models
│   │   ├── enums.py
│   │   └── result.py
│   ├── services
│   │   ├── __init__.py
│   │   └── banner_service.py
│   ├── templates
│   │   ├── __init__.py
│   │   ├── __version__.py
│   │   └── config.toml
│   ├── theme
│   │   ├── __init__.py
│   │   └── theme.py
│   ├── ui
│   │   ├── __init__.py
│   │   ├── console.py
│   │   ├── exceptions.py
│   │   ├── panels.py
│   │   ├── progress.py
│   │   └── tables.py
│   ├── utils
│   │   ├── logging.py
│   │   ├── parsing.py
│   │   ├── paths.py
│   │   └── resolver.py
│   ├── __init__.py
│   ├── __main__.py
│   └── __version__.py
├── docs
│   ├── architecture
│   │   ├── design-patterns.md
│   │   ├── diagrams.md
│   │   └── workflow.md
│   ├── developer-guide
│   │   ├── blackbox
│   │   │   └── ai-development-workflow.md
│   │   ├── tooling
│   │   │   └── ruff
│   │   │       ├── ruff-ignore.md
│   │   │       └── ruff-select.md
│   │   ├── developer-guide.md
│   │   ├── docker-workflow.md
│   │   ├── getting-started.md
│   │   └── make-workflow.md
│   ├── diagrams
│   │   ├── generated
│   │   │   ├── activity-scan.png
│   │   │   ├── architecture-overview.png
│   │   │   ├── cli-menu-design.png
│   │   │   ├── flowchart-error-handling.png
│   │   │   ├── init-workflow.png
│   │   │   ├── models-structure.png
│   │   │   ├── scan-algorithm-flow.png
│   │   │   └── use-case.png
│   │   ├── activity-scan.mmd
│   │   ├── architecture-overview.mmd
│   │   ├── cli-menu-design.mmd
│   │   ├── flowchart-error-handling.mmd
│   │   ├── init-workflow.mmd
│   │   ├── models-structure.mmd
│   │   ├── README.md
│   │   ├── scan-algorithm-flow.mmd
│   │   └── use-case.mmd
│   ├── project
│   │   ├── languages
│   │   │   ├── markdown-language-strategy.md
│   │   │   └── supported-languages.md
│   │   └── project-structure.md
│   ├── reads
│   │   ├── documentation-audit-report.md
│   │   ├── linting-vs-formatting.md
│   │   └── ruff.md
│   ├── testing
│   │   └── testing-guide.md
│   ├── user-guide
│   │   ├── commands.md
│   │   ├── installation-methods.md
│   │   ├── legacy-overview.md
│   │   ├── legacy-user-guide.md
│   │   ├── lifecycle.md
│   │   ├── overview.md
│   │   └── quickstart.md
│   ├── badges.md
│   ├── ci-cd.md
│   ├── configuration.md
│   ├── dry-run.md
│   ├── how-to-use.md
│   ├── index.md
│   ├── infrastructure.md
│   ├── installation.md
│   ├── project_structure.md
│   ├── TODO_tracking_history.md
│   └── usage.md
├── logs/ ... (collapsed)
├── make
│   ├── backups
│   │   └── Full_Makefile - 25082026
│   └── core
│       ├── build_publish
│       │   ├── command.mk
│       │   └── help.mk
│       ├── ci
│       │   ├── command.mk
│       │   └── help.mk
│       ├── cleanup
│       │   ├── command.mk
│       │   └── help.mk
│       ├── compose
│       │   ├── command
│       │   │   ├── common.mk
│       │   │   └── core.mk
│       │   └── help.mk
│       ├── docker
│       │   ├── command
│       │   │   ├── common.mk
│       │   │   └── core.mk
│       │   └── help.mk
│       ├── documentation
│       │   ├── command.mk
│       │   └── help.mk
│       ├── examples
│       │   └── help.mk
│       ├── git
│       │   ├── command.mk
│       │   └── help.mk
│       ├── help
│       │   ├── command.mk
│       │   ├── helper.mk
│       │   └── variable.mk
│       ├── helpers
│       │   ├── common.mk
│       │   └── registry.mk
│       ├── lint_format
│       │   ├── command.mk
│       │   └── help.mk
│       ├── local
│       │   ├── command.mk
│       │   └── help.mk
│       ├── qa
│       │   ├── command.mk
│       │   └── help.mk
│       ├── remote
│       │   ├── command
│       │   │   ├── registry.mk
│       │   │   └── runtime.mk
│       │   └── help.mk
│       ├── setup_install
│       │   ├── command.mk
│       │   └── help.mk
│       ├── testing
│       │   ├── command.mk
│       │   └── help.mk
│       └── variables
│           ├── help.mk
│           └── variable.mk
├── scripts
│   ├── ci
│   │   ├── __init__.py
│   │   └── package_version.py
│   ├── docker
│   │   ├── docker-remove-images.ps1
│   │   └── docker-remove-images.sh
│   ├── docs
│   │   ├── docs
│   │   │   └── render_mermaid_examples.md
│   │   ├── venv/ ... (collapsed)
│   │   ├── check_docs_links.py
│   │   └── render_mermaid.py
│   ├── repository
│   │   └── src
│   │       └── sync_metadata.py
│   └── __init__.py
├── site/ ... (collapsed)
├── tests
│   ├── cli
│   │   ├── test_init_command.py
│   │   ├── test_main.py
│   │   └── test_versions.py
│   ├── config
│   │   └── test_config_loader.py
│   ├── core
│   │   ├── build/ ... (collapsed)
│   │   ├── initialize
│   │   │   ├── test_init_builder.py
│   │   │   └── test_init_main.py
│   │   └── scan
│   │       ├── test_processor.py
│   │       ├── test_scanner.py
│   │       └── test_updater.py
│   ├── integration
│   │   └── test_full_scan.py
│   ├── languages
│   │   ├── test_html_strategy.py
│   │   ├── test_javascript_strategy.py
│   │   ├── test_php_strategy.py
│   │   ├── test_python_strategy.py
│   │   └── test_shell_strategy.py
│   ├── services
│   │   └── test_banner_service.py
│   ├── theme
│   │   └── test_theme.py
│   ├── unit
│   │   └── config
│   │       ├── test_precommit_config.py
│   │       └── test_pyproject_toml.py
│   ├── utils
│   │   ├── test_logging.py
│   │   ├── test_parsing.py
│   │   ├── test_paths.py
│   │   └── test_resolver.py
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_developer_workflows.py
│   └── test_dry_run.py
├── venv/ ... (collapsed)
├── .coverage
├── .dockerignore
├── .gitignore
├── .gitlab-ci.yml
├── .pre-commit-config.yaml
├── .prettierignore
├── .prettierrc.json
├── AGENTS.md
├── before.gitlab-ci.yml.before
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── docker-compose.yml
├── Dockerfile
├── ENGINEERING_EXECUTION_POLICY.md
├── example_command.txt
├── LICENSE
├── Makefile
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
├── SECURITY.md
├── TODO.md
└── Virtual
```

---

## Root Files

| File | Description |
|------|-------------|
| `README.md` | Project overview and introduction. |
| `CHANGELOG.md` | History of notable changes between releases. |
| `LICENSE` | Project license information. |
| `CONTRIBUTING.md` | Guidelines for contributing to the project. |
| `SECURITY.md` | Security policy and vulnerability reporting instructions. |
| `TODO.md` | Pending tasks and future improvements. |
| `AGENTS.md` | Instructions and guidance for AI agents and automation tools. |
| `ENGINEERING_EXECUTION_POLICY.md` | Engineering execution standards and policies. |
| `pyproject.toml` | Main Python project configuration file. |
| `requirements.txt` | Python package dependencies. |
| `mkdocs.yml` | MkDocs documentation site configuration. |
| `Makefile` | Defines common development, testing, and build commands. |
| `Dockerfile` | Container image build instructions. |
| `docker-compose.yml` | Default multi-container Docker configuration. |
| `docker-compose.dev.yml` | Development Docker Compose configuration. |
| `docker-compose.prod.yml` | Production Docker Compose configuration. |
| `.gitignore` | Specifies files and directories ignored by Git. |
| `.dockerignore` | Specifies files excluded from Docker build context. |
| `.prettierrc.json` | Prettier code formatting configuration. |
| `.prettierignore` | Files ignored by Prettier. |
| `.pre-commit-config.yaml` | Pre-commit hooks configuration. |
| `.gitlab-ci.yml` | GitLab CI/CD pipeline configuration. |

---

## Directory Details

### `.config/`
Project configuration files.

Stores reusable configuration files used by the project.
Helps keep the repository root clean and organized.

Common examples:
- .config/tool-config/
- .config/templates/
- .config/settings/

### `app/`
Main application source code.

Contains the core implementation of the project.
May include business logic, services, modules, and utilities.

### `docs/`
Project documentation and technical references.

The documentation folder usually contains structured knowledge about the project.

Common documentation sections:
- docs/architecture        → system design and architecture diagrams
- docs/development         → development guides and workflows
- docs/system              → detailed technical documentation
- docs/reference           → command references and APIs
- docs/user-guide          → instructions for end users
- docs/diagrams            → visual architecture diagrams
- docs/phases              → project phases and planning
- docs/Q&A                 → common questions and explanations

Common files:
- PROJECT_STRUCTURE.md
- DEVELOPMENT_GUIDE.md
- HOW_TO_USE.md
- TODO.md
- CLI_COMMAND.md
- references.md
- badges.md

### `scripts/`
Utility scripts for development or automation.

May include deployment scripts, maintenance tools, or helpers.

### `tests/`
Automated tests.

Contains unit tests and integration tests.
Ensures code reliability and correctness.


---

## Notes

- Temporary files, caches, and environment directories are excluded.
- Structure is generated automatically using DocGen.
