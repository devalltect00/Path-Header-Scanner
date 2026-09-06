# tests/utils/test_paths.py

"""Tests for path normalization, relative conversion, and display formatting."""

from pathlib import Path

import pytest

from app.utils.paths import format_display_path, normalize_path, to_relative_path


def test_to_relative_path_success(tmp_path: Path) -> None:
    """
    Verify files under root are converted to expected relative POSIX path.

    Args:
        tmp_path: Temporary filesystem root fixture.

    Returns:
        None
    """
    root = tmp_path
    file_path = tmp_path / "app" / "main.py"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("print('x')\n", encoding="utf-8")

    relative = to_relative_path(file_path=file_path, root_directory=root)
    assert relative == Path("app/main.py")


def test_to_relative_path_raises_when_outside_root(tmp_path: Path) -> None:
    """
    Verify conversion raises ValueError when file path is outside root.

    Args:
        tmp_path: Temporary filesystem root fixture.

    Returns:
        None

    Raises:
        ValueError: Expected when file is not under root directory.
    """
    root = tmp_path / "root"
    root.mkdir()
    outside = tmp_path / "outside.py"
    outside.write_text("x\n", encoding="utf-8")

    with pytest.raises(ValueError):
        to_relative_path(file_path=outside, root_directory=root)


def test_normalize_path_returns_posix() -> None:
    """
    Verify path normalization returns POSIX-style separators.

    Returns:
        None
    """
    assert normalize_path(Path("app") / "main.py") == "app/main.py"


def test_format_display_path_combines_relative_and_normalize(tmp_path: Path) -> None:
    """
    Verify display path formatting combines relative conversion and normalization.

    Args:
        tmp_path: Temporary filesystem root fixture.

    Returns:
        None
    """
    root = tmp_path
    file_path = tmp_path / "nested" / "index.php"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("<?php echo 'ok';\n", encoding="utf-8")

    assert (
        format_display_path(file_path=file_path, root_directory=root)
        == "nested/index.php"
    )
