# TODO

Personal planning and roadmap for **Path Header Scanner**.

---

## Features

### ✅ Completed

- [x] Build Path Header Scanner as a lightweight utility to insert, validate, and update file path headers across source and documentation files.
- [x] Implement core processing/scanning/update logic.
- [x] Implement CLI interface.
- [x] Add UI helper or help command.
- [x] Configure Git and repository metadata files.
- [x] Add CI pipelines (GitHub + GitLab).
- [x] Add Docker and Docker Compose configurations.
- [x] Separate Docker Compose development and production configurations.
- [x] Add project meta/support files (`CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`).
- [x] Add pre-commit configuration.
- [x] Add `Makefile`.
- [x] Add docs server setup with MkDocs.
- [x] Add automated tests.
- [x] Add the docs/TODO.md

---

### 🧩 In Progress

#### General

- [x] Add project banner.
- [x] Add external file configurations i.e. config.toml.
- [x] Add Init command
- [x] Add Tests for Init command
- [x] Add check project version arguments
- [x] Improve documentation theme/visual consistency.
- [x] Extend the logging system to support both console and file output.
- [x] Overall Update all docs inside docs/
  - [x] Add the docs/badges.md
  - [x] Add the docs/configuration.md
  - [x] Add the docs/how-to-use.md
  - [x] Add the docs/index.md
  - [x] Add the docs/infrastructure.md
  - [x] Add the docs/installation.md
  - [x] Add the docs/usage.md
  - [x] Add the docs/project_structure.md
  - [x] Add the diagrams to docs/diagrams/
- [x] Add the AGENTS.md
- [x] Make sure all the files inside below directories already patch with path-header-scanner
  - [x] app/
  - [x] docs/
  - [x] tests/
- [x] Add README.md
- [x] Improve and standardize documentation pages.
- [x] Link MkDocs navigation/config cleanly to all documentation folders.
- [x] Update `.gitignore` rules.
- [x] Update `.dockerignore` rules.
- [ ] Add `CHANGELOG.md`.
- [ ] General project cleanup and consistency pass.
- [x] Update pyproject.toml description
- [x] Update CONTRIBUTING.md description
- [x] Update Makefile
- [x] error exception on CLI when command is missing

#### Test Update Plan

- [x] Add CLI init command tests (`tests/cli/test_init_command.py`)
- [x] Extend CLI main callback tests for banner behavior (`tests/cli/test_main.py`)
- [x] Add banner service tests (`tests/services/test_banner_service.py`)
- [x] Add version callback tests (`tests/cli/test_versions.py`)
- [x] Add core initialize builder tests (`tests/core/initialize/test_init_builder.py`)
- [x] Add core initialize main execution tests (`tests/core/initialize/test_init_main.py`)
- [x] Run targeted pytest for updated/new test modules (including core/initialize)

---

### 🧠 Planned

#### 🚀 v1.0.0 release preparation

- [x] Establish `v1.0.0-rc.1` as the first formal release candidate; there is no previous supported production version.
- [x] Prepare separate internal commit messages and public tag/release messages for `v1.0.0-rc.1` and `v1.0.0`.
- [x] Align project metadata, Docker files, Docker Compose files, ignore rules, modular Make workflows, `AGENTS.md`, and documentation with the active application.
- [x] Add initialization and configuration scaffolding through `.config/path_header_scanner/config.toml`.
- [x] Add explicit dry-run behavior for initialization and scanning, with dry-run overriding CLI or configured apply mode.
- [x] Add regression coverage proving dry-run does not create scaffolding or modify scanned files.
- [x] Validate the current baseline with 121 passing tests, 83% coverage, Black, Ruff, and a Docker-based MkDocs build on Python 3.14.
- [ ] Validate `v1.0.0-rc.1` in disposable repositories across representative supported languages.
- [ ] Complete final cleanup and incorporate release-blocking corrections discovered during RC validation.
- [ ] Run final approved test, documentation, packaging, Make, Docker, Compose, and dry-run release checks.
- [ ] Commit, tag, publish, and verify `v1.0.0` only after explicit release approval.

#### 🧰 Future maintenance

- [ ] Review and update `.pre-commit-config.yaml` so hook versions, Python targets, and validation commands align with the current project. This is planning only; do not update the configuration as part of the v1.0.0 message-preparation work.

---

### 🔭 Future

- [ ] Break UI/frontend components into smaller, maintainable parts where the separation materially improves testing or extension.
- [ ] Add clearer scan/update progress visibility for large targets.
- [ ] Consider accepting multiple target directories in one scan while preserving deterministic path resolution and mutation safety.

---

### 🗑️ Cancelled / Dropped

- _(Nothing yet)_

---

## ⚖️ Considerations

- Use Pipeline Strategy for core / logic / backend sides
- Adding path_header_scanner configuration file
- Combine this / the project with another project into one project

---

## 💡 Ideas

- _(Nothing yet)_

---

## 🧾 Notes

### TODO.md

Keep this file concise, status-driven, and updated during each milestone.
