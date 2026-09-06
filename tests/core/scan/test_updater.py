# tests/core/scan/test_updater.py

"""
Tests for file updater.

This module validates:
- missing header insertion
- invalid header replacement
- valid header detection
- shebang preservation
- encoding preservation
- PHP opening tag preservation
- empty file handling
"""

from pathlib import Path

from app.core.scan.updater import FileUpdater
from app.languages.php import PhpLanguageStrategy
from app.languages.python import (
    PythonLanguageStrategy,
)
from app.models.enums import FileStatus

INCLUDE_TARGET_DIRECTORY = False


def test_insert_missing_python_header(
    tmp_path: Path,
) -> None:
    """
    Test insertion of missing Python header.

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

    updater = FileUpdater(tmp_path)

    result = updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    assert result.status == FileStatus.INSERTED

    assert "# main.py" in updated_content


def test_replace_invalid_python_header(
    tmp_path: Path,
) -> None:
    """
    Test replacement of invalid Python header.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        ('# wrong/path.py\n\nprint("hello")\n'),
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    result = updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    assert result.status == FileStatus.UPDATED

    assert "# main.py" in updated_content

    assert "# wrong/path.py" not in updated_content


def test_valid_python_header(
    tmp_path: Path,
) -> None:
    """
    Test detection of already valid header.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        ('# main.py\n\nprint("hello")\n'),
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    result = updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    assert result.status == FileStatus.VALID


def test_preserve_shebang(
    tmp_path: Path,
) -> None:
    """
    Test preservation of shebang line.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        ('#!/usr/bin/env python3\nprint("hello")\n'),
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    lines = updated_content.splitlines()

    assert lines[0] == "#!/usr/bin/env python3"

    assert lines[1] == "# main.py"


def test_preserve_encoding_header(
    tmp_path: Path,
) -> None:
    """
    Test preservation of encoding declaration.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        ('# -*- coding: utf-8 -*-\nprint("hello")\n'),
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    lines = updated_content.splitlines()

    assert lines[0] == "# -*- coding: utf-8 -*-"

    assert lines[1] == "# main.py"


def test_preserve_php_opening_tag(
    tmp_path: Path,
) -> None:
    """
    Test preservation of PHP opening tag.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "index.php"

    file_path.write_text(
        ('<?php\necho "hello";\n'),
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    updater.process_file(
        file_path=file_path,
        strategy=PhpLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    lines = updated_content.splitlines()

    assert lines[0] == "<?php"

    assert lines[1] == "// index.php"


def test_empty_python_file(
    tmp_path: Path,
) -> None:
    """
    Test insertion into empty Python file.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    file_path = tmp_path / "empty.py"

    file_path.write_text(
        "",
        encoding="utf-8",
    )

    updater = FileUpdater(tmp_path)

    result = updater.process_file(
        file_path=file_path,
        strategy=PythonLanguageStrategy(),
        apply_changes=True,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    updated_content = file_path.read_text(
        encoding="utf-8",
    )

    assert result.status == FileStatus.INSERTED

    assert "# empty.py" in updated_content
