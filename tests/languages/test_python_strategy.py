# tests/languages/test_python_strategy.py

"""
Tests for Python language strategy.

This module validates:
- supported extensions
- header generation
- header extraction
- insertion index logic
"""

from pathlib import Path

from app.languages.python import (
    PythonLanguageStrategy,
)


def test_python_strategy_extensions() -> None:
    """
    Test supported Python extensions.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    assert ".py" in strategy.extensions


def test_python_strategy_comment_prefix() -> None:
    """
    Test Python comment prefix.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    assert strategy.comment_prefix == "#"


def test_python_build_header() -> None:
    """
    Test Python header generation.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    header = strategy.build_header(Path("app/main.py"))

    assert header == "# app/main.py"


def test_python_extract_valid_header() -> None:
    """
    Test extraction of valid Python header.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        "# app/main.py",
        "",
        'print("hello")',
    ]

    header = strategy.extract_header(lines)

    assert header == "# app/main.py"


def test_python_extract_missing_header() -> None:
    """
    Test extraction when no header exists.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        'print("hello")',
    ]

    header = strategy.extract_header(lines)

    assert header is None


def test_python_shebang_insertion_index() -> None:
    """
    Test insertion index with shebang.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        "#!/usr/bin/env python3",
        'print("hello")',
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 1


def test_python_encoding_insertion_index() -> None:
    """
    Test insertion index with encoding declaration.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        "# -*- coding: utf-8 -*-",
        'print("hello")',
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 1


def test_python_shebang_and_encoding_index() -> None:
    """
    Test insertion index with shebang and encoding.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        "#!/usr/bin/env python3",
        "# -*- coding: utf-8 -*-",
        'print("hello")',
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 2


def test_python_extract_header_after_shebang() -> None:
    """
    Test header extraction after shebang line.

    Returns:
        None
    """

    strategy = PythonLanguageStrategy()

    lines = [
        "#!/usr/bin/env python3",
        "# app/main.py",
        "",
        'print("hello")',
    ]

    header = strategy.extract_header(lines)

    assert header == "# app/main.py"
