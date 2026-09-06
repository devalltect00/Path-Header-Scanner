<!-- docs/TODO_tracking_history_v1.0.0-rc.1.md -->

> Cumulative snapshot for **v1.0.0-rc.1**. Earlier tasks, unfinished work,
> considerations, ideas, cancelled items, and notes are intentionally retained.

# Path Header Scanner TODO Tracking History — v1.0.0-rc.1

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

## Since v1.0.0-rc.1

### Version context

| Field | Value |
| --- | --- |
| Version | `v1.0.0-rc.1` |
| Previous version | None — first formal release |
| Release type | First production release candidate |
| Version strategy | Semantic Versioning |
| Package compatibility | Python 3.11+ |
| Standard development/runtime | Python 3.14 |

### Completed release-candidate scope

#### Scanning and header management

- [x] Discover supported source and documentation files recursively.
- [x] Validate missing, current, and stale repository-relative path headers.
- [x] Insert or replace headers through language-aware strategies.
- [x] Support Python, JavaScript, TypeScript, Shell, PHP, HTML, and Markdown syntax.
- [x] Preserve relevant leading content, special lines, and trailing-newline behavior.
- [x] Apply configurable ignore rules for repositories, environments, caches, dependencies, build outputs, and user paths.
- [x] Report valid, inserted, updated, unsupported, skipped, and failed files clearly.

#### CLI, configuration, and safety

- [x] Add `path-header-scanner init` and `path-header-scanner scan <target>`.
- [x] Keep scan preview non-mutating by default and require `--apply` for file updates.
- [x] Add target, working-directory, logging, debug, banner, version, help, and completion controls.
- [x] Add `.config/path_header_scanner/config.toml` with CLI → configuration → default resolution.
- [x] Add initialization builders, models, registries, presenters, and scaffold generation.
- [x] Add Rich banners, help, panels, progress, summaries, and actionable command errors.
- [x] Add centralized CLI exception handling with reliable nonzero failure exits and debug-only tracebacks.

#### Dry-run guarantees

- [x] Add dry-run to initialization and scanning.
- [x] Make scan dry-run override both CLI `--apply` and configured `apply = true`.
- [x] Prevent dry-run initialization from creating directories, writing files, overwriting content, or prompting.
- [x] Keep read-only discovery, validation, and rendering available during simulation.
- [x] Add terminal messages that distinguish preview, dry-run, and live apply behavior.

#### Architecture and developer workflow

- [x] Separate CLI parsing and presentation from scan discovery, processing, validation, and updates.
- [x] Isolate language-specific behavior behind focused strategies.
- [x] Add shared results, domain exceptions, path and logging utilities, UI components, and themes.
- [x] Separate initialization planning from persistence so dry-run stops before mutation.
- [x] Add `AGENTS.md` and engineering guidance for scan safety, configuration, testing, and releases.
- [x] Add modular Make, Docker, Compose, CI/CD, packaging, Ruff, Black, Pytest, MkDocs, and pre-commit workflows.

#### Tests and documentation

- [x] Add CLI, configuration, initialization, scanner, processor, updater, language, service, UI, and utility tests.
- [x] Add regressions for preview/apply behavior, configuration precedence, and dry-run override behavior.
- [x] Add pre-commit configuration validation and command-help/developer-workflow checks.
- [x] Record the release baseline as 123 passing tests with 84% measured coverage on Python 3.14.
- [x] Document installation, configuration, usage, safety, languages, architecture, testing, Docker, Compose, Make, and troubleshooting.
- [x] Add dedicated dry-run guidance and project-structure/diagram documentation.
- [x] Prepare separate internal commit and public release messages for RC.1 and stable 1.0.0.

### RC validation checklist

#### CI/CD release safeguards completed for RC.1

- [x] Validate Python 3.11 and 3.14 in hosted CI.
- [x] Derive GHCR destinations from the active repository and use GitLab's project registry destination.
- [x] Build from the root multi-stage Dockerfile with explicit development or production targets.
- [x] Require a non-empty annotated SemVer tag before production image or provider-release publication.
- [x] Publish exact prerelease tags without updating `latest`; reserve `latest` for stable releases.
- [x] Preserve full annotated tag messages as provider release notes and attach package artifacts.
- [x] Pin Ruff and Black consistently and add workflow-contract regression tests.
- [x] Keep the comprehensive product commit as an untagged checkpoint and reserve the RC.1 tag for CI/CD finalization.

- [ ] Install RC.1 in an isolated environment and validate root and command help.
- [ ] Preview and perform initialization in a disposable repository.
- [ ] Scan representative files for every supported language in preview mode.
- [ ] Verify `--apply --dry-run` leaves every target file unchanged.
- [ ] Apply reviewed changes and inspect headers, special lines, and summaries.
- [ ] Validate custom ignores, working-directory resolution, unsupported files, and failure handling.
- [ ] Validate local, Docker, Compose, Make, package, and documentation workflows.
- [ ] Commit, tag, publish, and verify `v1.0.0-rc.1` only with explicit release approval.

### Deferred beyond RC.1

- [ ] Complete final cleanup and incorporate release-blocking RC corrections.
- [ ] Consider multiple target directories while preserving deterministic resolution and mutation safety.
- [ ] Improve progress visibility further if large-repository validation identifies a real need.
- [ ] Split UI components further only where it materially improves testing or extension.
- [ ] Review future pre-commit upgrades intentionally rather than updating them as a release side effect.

### Notes

- This is the first formal release line, so there is no supported earlier
  production release to migrate from.
- This snapshot does not claim that a tag, package, image, or release has been
  published.

---

## Additional status carried from repository TODO files

### CLI option modularization

- [x] Move initialization options into `app/cli/commands/init/options.py`.
- [x] Define and import `AskOption`, `ForceOption`, and `ModeOption` from the focused options module.
- [x] Keep command functions focused on orchestration rather than repeating option declarations.

The root `TODO.md` still uses unchecked boxes for this work, but the active
source contains the requested module and imports. This versioned history records
the implementation state without modifying the original TODO file.

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

### Path Header Scanner TODO Tracking History — v1.0.0-rc.1.md

Keep this file concise, status-driven, and updated during each milestone.
