# tests/core/scan/test_processor.py

"""
Tests for file processor.

This module validates:
- strategy resolution
- file processing orchestration
- result collection
- multi-file processing
"""

from pathlib import Path

from app.core.scan.processor import FileProcessor
from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)
from app.languages.python import (
    PythonLanguageStrategy,
)
from app.models.enums import FileStatus

INCLUDE_TARGET_DIRECTORY = True


def test_processor_resolves_python_strategy(
    tmp_path: Path,
) -> None:
    """
    Test strategy resolution for Python files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    file_path = tmp_path / "main.py"

    strategy = processor._resolve_strategy(
        file_path=file_path,
    )

    assert strategy is not None

    assert strategy.__class__.__name__ == "PythonLanguageStrategy"


def test_processor_resolves_javascript_strategy(
    tmp_path: Path,
) -> None:
    """
    Test strategy resolution for JavaScript files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=[
            JavaScriptLanguageStrategy(),
        ],
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    file_path = tmp_path / "main.js"

    strategy = processor._resolve_strategy(
        file_path=file_path,
    )

    assert strategy is not None

    assert strategy.__class__.__name__ == "JavaScriptLanguageStrategy"


def test_processor_returns_results(
    tmp_path: Path,
) -> None:
    """
    Test processor returns processing results.

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

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    results = processor.process_files(
        files=[file_path],
        apply_changes=True,
    )

    assert len(results) == 1

    assert results[0].status == FileStatus.INSERTED


def test_processor_multiple_files(
    tmp_path: Path,
) -> None:
    """
    Test processing multiple files.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_a = tmp_path / "a.py"
    file_b = tmp_path / "b.py"

    file_a.write_text(
        'print("a")\n',
        encoding="utf-8",
    )

    file_b.write_text(
        'print("b")\n',
        encoding="utf-8",
    )

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    results = processor.process_files(
        files=[file_a, file_b],
        apply_changes=True,
    )

    assert len(results) == 2

    assert all(result.status == FileStatus.INSERTED for result in results)


def test_processor_skips_unknown_extension(
    tmp_path: Path,
) -> None:
    """
    Test processor skips unsupported files.

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

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=[
            PythonLanguageStrategy(),
        ],
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    results = processor.process_files(
        files=[file_path],
        apply_changes=True,
    )

    assert results == []
