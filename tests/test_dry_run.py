# tests/test_dry_run.py

"""Dry-run resolution regression tests for Path Header Scanner."""

from types import SimpleNamespace

from app.cli.commands.scan.resolver import resolve_scan_args
from app.config.config_loader import ConfigLoader


def test_configured_dry_run_overrides_configured_apply(tmp_path) -> None:
    """Configured dry-run must keep scan non-mutating when apply is enabled."""

    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.path-header-scanner.cli.execution]
dry_run = true

[tool.path-header-scanner.cli.scan]
apply = true
""".strip(),
        encoding="utf-8",
    )
    config = ConfigLoader(filename=config_file)
    cli_args = SimpleNamespace(
        target_directory=".",
        workdir=None,
        apply=None,
        dry_run=None,
        include_target_directory=None,
        debug=None,
    )

    args = resolve_scan_args(config, cli_args)

    assert args.dry_run is True
    assert args.apply is False


def test_explicit_no_dry_run_overrides_configuration(tmp_path) -> None:
    """Explicit no-dry-run should restore separately authorized apply mode."""

    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.path-header-scanner.cli.execution]
dry_run = true

[tool.path-header-scanner.cli.scan]
apply = true
""".strip(),
        encoding="utf-8",
    )
    config = ConfigLoader(filename=config_file)
    cli_args = SimpleNamespace(
        target_directory=".",
        workdir=None,
        apply=None,
        dry_run=False,
        include_target_directory=None,
        debug=None,
    )

    args = resolve_scan_args(config, cli_args)

    assert args.dry_run is False
    assert args.apply is True
