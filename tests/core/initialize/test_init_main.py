# tests/core/initialize/test_init_main.py

"""Tests for InitMain orchestration of initialization generation flow."""

from pathlib import Path
from types import SimpleNamespace

from app.cli.constants.enums import InitMode
from app.core.initialize.main import InitMain
from app.core.initialize.models.initialization_result import (
    InitializationResult,
)


def test_init_main_executes_generator_with_built_spec(monkeypatch) -> None:
    """
    Verify InitMain builds spec and invokes ScaffoldGenerator with expected args.

    Args:
        monkeypatch: Pytest fixture used to replace ScaffoldGenerator class.

    Returns:
        None
    """
    captured = {}

    class FakeGenerator:
        def __init__(self, force, interactive):
            captured["force"] = force
            captured["interactive"] = interactive

        def run(
            self,
            mode,
            templates,
            dirs,
            template_dirs,
        ):
            captured["mode"] = mode
            captured["templates"] = templates
            captured["dirs"] = dirs
            captured["template_dirs"] = template_dirs

            return InitializationResult(
                mode=mode,
                created_files=0,
                copied_files=0,
                skipped_files=0,
                created_directories=0,
            )

    monkeypatch.setattr(
        "app.core.initialize.main.ScaffoldGenerator",
        FakeGenerator,
    )

    args = SimpleNamespace(
        mode=InitMode.ALL,
        force_init=True,
        ask=False,
        dry_run=False,
        debug=True,
        log_level="info",
    )

    InitMain().execute(args)

    assert captured["force"] is True
    assert captured["interactive"] is False
    assert len(captured["templates"]) == 1
    assert captured["templates"][0].target_path == Path(
        ".config/path_header_scanner/config.toml"
    )
    assert ".config/path_header_scanner" in captured["dirs"]


def test_init_main_dry_run_does_not_create_files(tmp_path, monkeypatch) -> None:
    """Dry-run previews initialization without creating project files."""

    monkeypatch.chdir(tmp_path)
    args = SimpleNamespace(
        mode=InitMode.ALL,
        force_init=True,
        ask=True,
        dry_run=True,
        debug=True,
        log_level="info",
    )

    InitMain().execute(args)

    assert not (tmp_path / ".config").exists()
