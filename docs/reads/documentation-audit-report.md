<!-- docs/reads/documentation-audit-report.md -->

# Documentation Audit Report

## Scope

Audited all files under `docs/` and validated against implementation in:

- `app/` (primary entrypoint: `app/cli/main.py`)
- `tests/`

Protected files were reviewed for reference only and not modified:

- `docs/badges.md`
- `docs/configuration.md`
- `docs/infrastructure.md`
- `docs/installation.md`
- `docs/usage.md`

---

## Executive Summary

The documentation has strong coverage intent, but currently suffers from **drift** and **navigation inconsistency**:

1. `docs/index.md` references multiple files that do not exist.
2. Several documents use stale path labels (e.g., `docs/path-header/...`) in headings/comments.
3. CLI docs partially mismatch current implementation details (especially `init --mode` values).
4. User docs contain overlapping/legacy pages with unclear canonical flow.
5. Architecture and developer docs are detailed but partially repetitive and not consistently aligned in naming and cross-links.
6. Testing docs are present but need closer mapping to current `tests/` tree and practical command usage.

---

## Findings by Category

## 1) Navigation and Broken References

### Issues found

- `docs/index.md` links to non-existent files:
    - `docs/developer-guide/development-workflow.md`
    - `docs/developer-guide/testing-guide.md`
    - `docs/developer-guide/contributing-notes.md`
    - `docs/architecture/system-overview.md`
    - `docs/architecture/cli-flow.md`
    - `docs/architecture/module-dependencies.md`
    - `docs/project/app-overview.md`
    - `docs/project/module-map.md`
    - `docs/testing/strategy-and-coverage.md`

### Recommendation

- Replace with existing files or create missing docs where they provide value.
- Establish a canonical landing map in `docs/index.md`.

---

## 2) Accuracy vs CLI Implementation

Validated against:

- `app/cli/main.py`
- `app/cli/commands/init/*`
- `app/cli/commands/scan/*`
- `app/cli/constants/enums.py`

### Issues found

- `init --mode` docs mention values not present in `InitMode` enum:
    - code currently includes: `all`, `config`
    - docs mention: `templates`, `examples`, `all_no_examples`
- Must reflect actual options exposed by current implementation.

### Confirmed accurate items

- Main commands exist: `init`, `scan`
- Global options include `--help`, `--no-banner`, `--version`
- Scan options include:
    - `--workdir`
    - `--apply`
    - `--include-target-directory/--exclude-target-directory`
    - `--debug`

---

## 3) Content Quality and Consistency

### Issues found

- Inconsistent document headers/comments:
    - Some files start with outdated labels like `docs/path-header/...`.
- Terminology drift:
    - “Path Header Scanner” vs “Path-Header-Scanner” used inconsistently.
- Repetition:
    - Architecture/developer files duplicate flow descriptions.
- Legacy docs:
    - `docs/user-guide/legacy-overview.md`
    - `docs/user-guide/legacy-user-guide.md`
      likely overlap with modern user docs and should be merged or archived.

### Recommendation

- Normalize naming to one canonical style.
- Keep one primary source for each concern and cross-link instead of duplicating.

---

## 4) Developer Documentation Coverage

### Current state

Developer docs exist under `docs/developer-guide/`, including tooling and AI workflow notes.

### Gaps

- Missing unified “developer workflow” page that ties:
    - setup
    - lint/test
    - docs contribution rules
    - release/dev loop

### Recommendation

- Keep existing useful pages, add missing glue docs, remove overlap.

---

## 5) User Documentation Coverage

### Current state

Good user-oriented set exists:

- overview
- quickstart
- commands
- installation methods
- lifecycle
- legacy pages

### Gaps / improvements

- Need clearer “first-run path” centered around:
    - install method choices
    - `--help`
    - `init`
    - dry-run `scan`
    - `--apply`
- Need better “requirements/prerequisites” page for runtime options (make/docker/python/wheel/tar.gz).

---

## 6) Testing Documentation Coverage

### Current state

`docs/testing/testing-guide.md` exists.

### Gaps

- Should map more directly to current `tests/` directories:
    - `tests/cli/`
    - `tests/core/`
    - `tests/integration/`
    - `tests/languages/`
    - `tests/utils/`
    - etc.
- Should include practical command examples used by contributors.

---

## 7) Diagram Coverage (.mmd / Mermaid)

### Current state

Architecture diagrams page exists but requires validation and standardization.

### Recommendation

- Keep Mermaid embedded in Markdown for maintainability.
- Add/update:
    - CLI execution flow
    - module dependency map
    - scan processing pipeline

---

## Missing / Recommended Documents

Recommended additions or refactors:

1. `docs/architecture/system-overview.md` (create)
2. `docs/architecture/cli-flow.md` (create)
3. `docs/architecture/module-dependencies.md` (create)
4. `docs/developer-guide/development-workflow.md` (create)
5. `docs/developer-guide/testing-guide.md` (create or move/alias to testing section)
6. `docs/project/app-overview.md` (create)
7. `docs/project/module-map.md` (create)
8. `docs/testing/strategy-and-coverage.md` (create)
9. `docs/user-guide/requirements.md` (create)
10. Merge or remove legacy user pages if no unique value remains.

---

## Proposed Final Structure (Target)

```text
docs/
├── index.md
├── badges.md                        (protected)
├── configuration.md                 (protected)
├── infrastructure.md                (protected)
├── installation.md                  (protected)
├── usage.md                         (protected)
├── architecture/
│   ├── system-overview.md
│   ├── cli-flow.md
│   ├── module-dependencies.md
│   ├── workflow.md
│   ├── design-patterns.md
│   └── diagrams.md
├── developer-guide/
│   ├── developer-guide.md
│   ├── getting-started.md
│   ├── development-workflow.md
│   ├── docker-workflow.md
│   ├── testing-guide.md
│   ├── blackbox/
│   │   └── ai-development-workflow.md
│   └── tooling/
│       └── ruff/
│           ├── ruff-ignore.md
│           └── ruff-select.md
├── project/
│   ├── app-overview.md
│   ├── module-map.md
│   ├── project-structure.md
│   └── languages/
│       ├── supported-languages.md
│       └── markdown-language-strategy.md
├── testing/
│   ├── testing-guide.md
│   └── strategy-and-coverage.md
├── user-guide/
│   ├── overview.md
│   ├── quickstart.md
│   ├── commands.md
│   ├── installation-methods.md
│   ├── lifecycle.md
│   └── requirements.md
└── reads/
    ├── documentation-audit-report.md
    ├── linting-vs-formatting.md
    └── ruff.md
```

---

## Refactor Priorities

1. Fix index navigation and broken links.
2. Correct CLI option docs to match implementation.
3. Consolidate/replace legacy user pages.
4. Add missing architecture and project overview docs.
5. Align testing docs with actual `tests/` layout.
6. Normalize terminology, headings, and internal links.
