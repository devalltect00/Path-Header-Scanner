# tests/cli/test_versions.py

"""Tests for CLI version callback behavior and output handling."""

import pytest
import typer

from app.cli.utils import versions


def test_version_callback_prints_and_exits(monkeypatch, capsys) -> None:
    """
    Verify version callback prints version information and exits.

    Args:
        monkeypatch: Pytest fixture to patch version provider.
        capsys: Pytest fixture for stdout/stderr capture.

    Returns:
        None

    Raises:
        typer.Exit: Expected when callback is invoked with True.
    """
    monkeypatch.setattr(
        versions.banner,
        "get_version",
        lambda: "2.0.0",
    )

    with pytest.raises(typer.Exit):
        versions.version_callback(True)

    captured = capsys.readouterr()
    assert "Path Header Scanner" in captured.out
    assert "2.0.0" in captured.out


def test_version_callback_noop_when_false(capsys) -> None:
    """
    Verify version callback performs no output when flag is False.

    Args:
        capsys: Pytest fixture for stdout/stderr capture.

    Returns:
        None
    """
    versions.version_callback(False)
    captured = capsys.readouterr()
    assert captured.out == ""
