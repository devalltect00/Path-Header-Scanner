# tests/languages/test_php_strategy.py

"""
Tests for PHP language strategy.

This module validates:
- supported extensions
- comment syntax
- PHP opening tag handling
- shebang handling
- header generation
- header extraction
"""

from pathlib import Path

from app.languages.php import (
    PhpLanguageStrategy,
)


def test_php_strategy_extensions() -> None:
    """
    Test supported PHP extensions.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    assert ".php" in strategy.extensions


def test_php_comment_prefix() -> None:
    """
    Test PHP comment prefix.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    assert strategy.comment_prefix == "//"


def test_php_build_header() -> None:
    """
    Test PHP header generation.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    header = strategy.build_header(Path("app/index.php"))

    assert header == "// app/index.php"


def test_php_extract_valid_header() -> None:
    """
    Test extraction of valid PHP header.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    lines = [
        "<?php",
        "// app/index.php",
        "",
        'echo "hello";',
    ]

    header = strategy.extract_header(lines)

    assert header == "// app/index.php"


def test_php_extract_missing_header() -> None:
    """
    Test extraction when no header exists.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    lines = [
        "<?php",
        'echo "hello";',
    ]

    header = strategy.extract_header(lines)

    assert header is None


def test_php_insertion_index_after_php_tag() -> None:
    """
    Test insertion index after PHP opening tag.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    lines = [
        "<?php",
        'echo "hello";',
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 1


def test_php_shebang_and_php_tag_index() -> None:
    """
    Test insertion index with shebang and PHP tag.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    lines = [
        "#!/usr/bin/php",
        "<?php",
        'echo "hello";',
    ]

    index = strategy.get_insertion_index(lines)

    assert index == 2


def test_php_extract_header_after_shebang() -> None:
    """
    Test header extraction after shebang and PHP tag.

    Returns:
        None
    """

    strategy = PhpLanguageStrategy()

    lines = [
        "#!/usr/bin/php",
        "<?php",
        "// app/index.php",
        "",
        'echo "hello";',
    ]

    header = strategy.extract_header(lines)

    assert header == "// app/index.php"
