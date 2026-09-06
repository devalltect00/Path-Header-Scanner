# TODO

> Cumulative snapshot for **v1.0.0-rc.1**. Earlier tasks, unfinished work,
> considerations, ideas, cancelled items, and notes are intentionally retained.

# Path Header Scanner TODO Tracking History — v1.0.0-rc.1

> Current status: see the [2026-09-06 checkpoint update](#checkpoint-4-2026-09-06).
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

## Since v1.0.0-rc.1

### Version context

| Field                        | Value                              |
| ---------------------------- | ---------------------------------- |
| Version                      | `v1.0.0-rc.1`                      |
| Previous version             | None — first formal release        |
| Release type                 | First production release candidate |
| Version strategy             | Semantic Versioning                |
| Package compatibility        | Python 3.11+                       |
| Standard development/runtime | Python 3.14                        |

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

---

<a id="checkpoint-4-2026-09-06"></a>

## 2026-09-06 status update — untagged checkpoint 4

Version scope: **v1.0.0-rc.1**.
The [checkpoint commit message](../.config/custy/templates/commit-message-v1.0.0-development-checkpoint-4.txt)
has **no associated tag or tag message**. It becomes part of the cumulative
RC.1 and stable release history.

### ✅ GitHub release-note rendering

- [x] Replace fragile shell-interpreted Markdown output with explicit `printf` generation so backticks remain literal release content.
- [x] Preserve the complete reviewed annotated tag message as the main GitHub Release description.
- [x] Populate version, release type, repository, commit, and workflow metadata instead of leaving empty placeholders.
- [x] Present concise literal Docker pull and Path Header Scanner CLI verification commands instead of transient image-download or runner output.
- [x] Preserve exact prerelease image tags and stable-only `latest` behavior.
- [x] Add regression coverage for release-note construction and keep the GitLab release workflow unchanged.

### ✅ Validation recorded

- [x] Complete Path Header Scanner test suite: 126 passed with 84% overall coverage.
- [x] Targeted release-workflow regression checks passed.
- [x] Pre-commit validation passed for the checkpoint and cumulative release-message templates.
- [x] Diff whitespace and mirrored-template consistency checks passed.
- [x] Record the maintainer's confirmation that the published GitHub RC page renders the annotated notes, metadata, and Docker guidance cleanly. This is historical reported validation, not a new provider operation for this checkpoint.

### Notes and evidence

- [GitHub release workflow](../.github/workflows/release.yml) contains the corrected release-note generation.
- [Checkpoint 4 commit message](../.config/custy/templates/commit-message-v1.0.0-development-checkpoint-4.txt) records the internal implementation details.
- The cumulative RC.1 and v1.0.0 commit and tag messages include checkpoint 4; this checkpoint itself remains untagged.
- No existing history, plans, ideas, cancelled work, or earlier checkpoint evidence was removed.
