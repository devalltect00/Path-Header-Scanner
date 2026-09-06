# Diagrams

This directory contains Mermaid source diagrams (`.mmd`) for Path Header Scanner.

## Scope

These diagrams are derived from the current implementation under `app/` and are intended to support:

- architecture understanding
- command/menu navigation understanding
- use-case communication
- algorithm/workflow explanation
- activity/flowchart views for operations and error handling

## Diagram Index

- `architecture-overview.mmd`
  High-level component architecture of the application packages.

- `use-case.mmd`
  Primary user/developer use cases for CLI operations.

- `cli-menu-design.mmd`
  CLI command/menu map based on Typer entrypoint and commands.

- `models-structure.mmd`
  Model-level structure and relationships (non-database domain models).

- `scan-algorithm-flow.mmd`
  Main scanning and header-processing algorithm flow.

- `init-workflow.mmd`
  Initialization command workflow (`init`) from CLI to generated artifacts.

- `activity-scan.mmd`
  Activity diagram for end-to-end scan lifecycle.

- `flowchart-error-handling.mmd`
  Error/result status handling and continuation behavior.

## Render Mermaid to Images/PDF

Use the reusable script:

```bash
python scripts/docs/render_mermaid.py
```

Default behavior:

- input dir: `docs/diagrams`
- output dir: `docs/diagrams/generated`
- input glob: `*.mmd`
- format: `png`
- non-recursive scan

### Common usage

Render all diagrams to PNG (default):

```bash
python scripts/docs/render_mermaid.py
```

Render to SVG:

```bash
python scripts/docs/render_mermaid.py --format svg
```

Render to PDF:

```bash
python scripts/docs/render_mermaid.py --format pdf
```

Custom input and output paths (reusable for other projects):

```bash
python scripts/docs/render_mermaid.py --input-dir path/to/diagrams --output-dir path/to/output
```

Recursive search in nested folders:

```bash
python scripts/docs/render_mermaid.py --recursive
```

Clean output directory before rendering:

```bash
python scripts/docs/render_mermaid.py --clean
```

Disable progress bar (CI/plain logs):

```bash
python scripts/docs/render_mermaid.py --no-progress
```

Use explicit Mermaid CLI path:

```bash
python scripts/docs/render_mermaid.py --mmdc "C:/tools/mmdc.cmd"
```

Extra render options:

```bash
python scripts/docs/render_mermaid.py --theme neutral --background transparent --width 1920 --height 1080 --scale 2
```

### Requirements

Install Mermaid CLI:

```bash
npm install -g @mermaid-js/mermaid-cli
```

Validate:

```bash
mmdc --version
```

### Output behavior

- The script mirrors subfolder structure from input to output.
- Returns exit code `0` when all files succeed.
- Returns exit code `1` when one or more files fail.

## Notes

- This project does **not** use a database; model diagrams represent domain/result structures only.
- Diagram sources here are intentionally separated from prose docs for easier maintenance.
- Update these files whenever command behavior, core processing flow, or model responsibilities change.
