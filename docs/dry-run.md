# Dry-run safety

Path Header Scanner supports explicit dry-run simulation on every command that
can change project files.

## Command behavior

| Command | Normal mutation | Dry-run behavior |
| --- | --- | --- |
| `path-header-scanner init` | Creates or updates `.config/path_header_scanner/config.toml` | Shows planned directories and files without creating, overwriting, or prompting |
| `path-header-scanner scan TARGET` | Preview-only by default | Performs read-only discovery and reports proposed header changes |
| `path-header-scanner scan TARGET --apply` | Writes approved header changes | Adding `--dry-run` overrides `--apply` and prevents every target-file write |

Examples:

```bash
path-header-scanner init --dry-run
path-header-scanner scan app --dry-run
path-header-scanner scan app --apply --dry-run
```

The last command remains non-mutating. Explicit dry-run always wins over
`--apply` and over `apply = true` from configuration.

## Configuration

Dry-run can be enabled for all commands in `.config/path_header_scanner/config.toml`:

```toml
[tool.path-header-scanner.cli.execution]
dry_run = true
```

Resolution order is:

1. command-line option (`--dry-run` or `--no-dry-run`)
2. `[tool.path-header-scanner.cli.execution].dry_run`
3. built-in default (`false`)

Use `--no-dry-run` only when you intentionally want to override configured
dry-run mode. Scan still needs `--apply` before it can write.

## Guaranteed boundary

During dry-run, safe discovery and validation may execute, but Path Header
Scanner does not:

- create or overwrite initialization files;
- create initialization directories;
- prompt for overwrite confirmation;
- insert or replace path headers;
- persist any target source or documentation changes.

Diagnostic logging may still write to the configured log destination. This is
operational telemetry, not a target-project mutation.

## Automation through Make

Pass the same CLI option through the existing argument variables:

```bash
make l-init PHS_INIT_ARGS="--dry-run"
make l-scan-apply TARGET=app PHS_SCAN_ARGS="--dry-run"
make d-init PHS_INIT_ARGS="--dry-run"
make c-scan-apply TARGET=app PHS_SCAN_ARGS="--dry-run"
```

The dry-run boundary is enforced by the application, so local, Docker, and
Compose execution have the same behavior.
