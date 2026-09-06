# TODO

> Current status: see the [2026-09-02 checkpoint update](#checkpoint-3-2026-09-02).
> Older checkboxes, test counts, plans, and decisions are preserved as recorded;
> they are historical context, not proof that every current release gate passed.

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

---

<a id="checkpoint-3-2026-09-02"></a>

## 2026-09-02 status update — untagged checkpoint 3

Version scope: **v1.0.0-rc.1**.
The [checkpoint commit message](../.config/custy/templates/commit-message-v1.0.0-development-checkpoint-3.txt)
has **no associated tag or tag message**. Earlier checkpoint files remain unchanged.

### ✅ Current application and developer workflow

- [x] Keep this as the first formal release line; temporary development tags do not establish an earlier supported release.
- [x] Keep preview-first scanning, explicit application, and `--dry-run` overriding both CLI and configured apply mode.
- [x] Retain target resolution, namespaced configuration, language-specific header preservation, and centralized CLI error handling.
- [x] Keep Python 3.11+ runtime compatibility and Python 3.14 as the standard development/container runtime.

The older root `TODO.md` CLI-modularization notes remain references rather
than a second current task list. Existing versioned entries record that work;
remaining scanner and multi-target ideas are retained.

### ✅ Delivery work carried forward

- [x] Align local, Docker/Compose, Make, pre-commit, and hosted CI validation with the active project rather than the old standalone layout.
- [x] Validate annotated release-tag metadata and package versions; publish exact prerelease/stable image tags and update `latest` only for stable releases.
- [x] Add private GitLab Python package build, artifact checks, clean-install verification, and protected-tag publication using `CI_JOB_TOKEN`.
- [x] Normalize supported release tags to PEP 440 package versions; reject unsupported or ambiguous versions rather than guessing.
- [x] Keep unprotected GitLab tag pipelines validation-only, skipping production-image, package-upload, and provider-release jobs.
- [x] Document installation of an available package version from the selected project registry, independently of cloning source or pulling a container.
- [x] Record the maintainer's report that hosted pipelines passed and the GitLab package registry was populated. This is historical reported validation, not a new pipeline run for this documentation checkpoint.

### ✅ Optional repository metadata helper

- [x] Add `scripts/repository/src/sync_metadata.py` outside the core application and installed CLI.
- [x] Read `[project].description` and independent GitHub/GitLab topics from `pyproject.toml`; do not reinterpret package keywords as repository topics.
- [x] Resolve one repository per provider from ordered remote candidates; the current defaults are GitHub `origin` and GitLab `backup`, using fetch URLs.
- [x] Provide a `--dry-run` path with read-only Git discovery and no provider API calls.
- [x] Document authenticated `gh`/`glab` for live updates, topic replacement and empty-list clearing, no confirmation prompt, and possible partial updates on failure.
- [x] Refresh the README against active commands, configuration, runtime requirements, installation methods, and the helper's actual `src/` path.
- [x] Keep helper details in checkpoint/release commit messages; leave user-facing tag-message templates unchanged for this maintainer-only addition.

### ⏳ Follow-up and release gates

- [ ] Correct the helper docstring examples that omit `src/` and reconcile its GitHub topic-limit constant (currently 50) with the provider maximum of 20.
- [ ] Add isolated mocked coverage for metadata validation, remote selection, dry-run API suppression, topic clearing, and provider failures before treating the helper as fully validated.
- [ ] Review actual targets, credentials, topic lists, and provider permissions before a separately authorized live metadata synchronization; no live synchronization was performed for this checkpoint.
- [ ] Re-run the relevant checks against the exact candidate commit before creating the v1.0.0-rc.1 tag. A passing temporary-tag pipeline is not a formal release.
- [ ] Complete the RC review and approved stable cleanup, then validate the final v1.0.0 commit before its release tag.
- [ ] Review and update pre-commit configuration in a future maintenance task. Existing pre-commit setup is complete; this pending item means a later refresh, not that hooks were never configured.

### Notes and evidence

- [README](../README.md) and [metadata helper](../scripts/repository/src/sync_metadata.py) describe the current setup.
- [GitLab package pipeline](../.gitlab/python-package.yml) defines the validation/publication boundary.
- Earlier test/coverage figures and release-checklist statuses remain attached to their original milestones.
- No existing history, ideas, alternatives, cancelled work, backup snapshots, or earlier checkpoint messages were removed.
