# tests/utils/test_resolver.py

"""Tests for target path resolution behavior in app.utils.resolver."""

from pathlib import Path

import pytest

from app.utils.resolver import resolve_target_path


def test_resolve_target_path_absolute(tmp_path: Path) -> None:
    """
    Resolve an absolute target path and verify canonical output.

    Args:
        tmp_path: Temporary directory fixture from pytest.

    Returns:
        None
    """
    target = tmp_path / "file.py"
    target.write_text("print('ok')\n", encoding="utf-8")

    resolved = resolve_target_path(str(target))
    assert resolved == target.resolve()


def test_resolve_target_path_with_working_directory(tmp_path: Path) -> None:
    """
    Resolve a relative target path using an explicit working directory.

    Args:
        tmp_path: Temporary directory fixture from pytest.

    Returns:
        None
    """
    workdir = tmp_path / "workspace"
    workdir.mkdir()
    target = workdir / "src"
    target.mkdir()

    resolved = resolve_target_path("src", working_directory=workdir)
    assert resolved == target.resolve()


def test_resolve_target_path_not_found_raises() -> None:
    """
    Raise FileNotFoundError when the target cannot be resolved.

    Returns:
        None
    """
    with pytest.raises(FileNotFoundError) as exc:
        resolve_target_path("this-path-should-not-exist-12345")

    message = str(exc.value)
    assert "Target path does not exist" in message
    assert "Attempted Locations" in message
