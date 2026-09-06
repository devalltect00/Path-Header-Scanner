# tests/core/scan/test_scanner.py

"""
Tests for file scanner.

This module validates:
- recursive scanning
- ignored directory handling
- supported extension detection
- unsupported file filtering
"""

from pathlib import Path

from app.constants.path import (
    THIS_PROJECT_SOURCE,
)
from app.core.scan.scanner import FileScanner
from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)
from app.languages.python import (
    PythonLanguageStrategy,
)


def test_scanner_finds_python_files(
    tmp_path: Path,
) -> None:
    """
    Test scanner finds Python files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        'print("hello")\n',
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert file_path in files


def test_scanner_finds_javascript_files(
    tmp_path: Path,
) -> None:
    """
    Test scanner finds JavaScript files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.js"

    file_path.write_text(
        'console.log("hello");\n',
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            JavaScriptLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert file_path in files


def test_scanner_ignores_unsupported_files(
    tmp_path: Path,
) -> None:
    """
    Test scanner ignores unsupported files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "README.md"

    file_path.write_text(
        "# Hello\n",
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert file_path not in files


def test_scanner_ignores_git_directory(
    tmp_path: Path,
) -> None:
    """
    Test scanner ignores .git directory.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    git_directory = tmp_path / ".git"

    git_directory.mkdir()

    file_path = git_directory / "hidden.py"

    file_path.write_text(
        'print("hello")\n',
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert file_path not in files


def test_scanner_recursive_scan(
    tmp_path: Path,
) -> None:
    """
    Test recursive directory scanning.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    nested_directory = tmp_path / THIS_PROJECT_SOURCE / "core"

    nested_directory.mkdir(
        parents=True,
    )

    file_path = nested_directory / "main.py"

    file_path.write_text(
        'print("hello")\n',
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert file_path in files


def test_scanner_returns_sorted_files(
    tmp_path: Path,
) -> None:
    """
    Test scanner returns sorted file list.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_b = tmp_path / "b.py"
    file_a = tmp_path / "a.py"

    file_b.write_text(
        'print("b")\n',
        encoding="utf-8",
    )

    file_a.write_text(
        'print("a")\n',
        encoding="utf-8",
    )

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
    )

    files = scanner.scan()

    assert files == sorted(files)
