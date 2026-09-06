# tests/languages/test_shell_strategy.py

"""
Tests for shell language strategy.

This module validates:
- supported extensions
- comment syntax
- shebang handling
- header generation
- header extraction
"""

from pathlib import Path

from app.languages.shell import (
    ShellLanguageStrategy,
)


def test_shell_strategy_extensions() -> None:
    """
    Test supported shell extensions.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    assert ".sh" in strategy.extensions
    assert ".bash" in strategy.extensions
    assert ".zsh" in strategy.extensions


def test_shell_comment_prefix() -> None:
    """
    Test shell comment prefix.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    assert strategy.comment_prefix == "#"


def test_shell_build_header() -> None:
    """
    Test shell header generation.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    header = strategy.build_header(Path("scripts/run.sh"))

    assert header == "# scripts/run.sh"


def test_shell_extract_valid_header() -> None:
    """
    Test extraction of valid shell header.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    lines = [
        "# scripts/run.sh",
        "",
        "echo hello",
    ]

    header = strategy.extract_header(lines)

    assert header == "# scripts/run.sh"


def test_shell_extract_missing_header() -> None:
    """
    Test extraction when no header exists.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    lines = [
        "echo hello",
    ]

    header = strategy.extract_header(lines)

    assert header is None


def test_shell_shebang_insertion_index() -> None:
    """
    Test insertion index with shebang.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    lines = [
        "#!/bin/bash",
        "echo hello",
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 1


def test_shell_extract_header_after_shebang() -> None:
    """
    Test header extraction after shebang.

    Returns:
        None
    """

    strategy = ShellLanguageStrategy()

    lines = [
        "#!/bin/bash",
        "# scripts/run.sh",
        "",
        "echo hello",
    ]

    header = strategy.extract_header(lines)

    assert header == "# scripts/run.sh"
