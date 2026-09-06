# tests/languages/test_javascript_strategy.py

"""
Tests for JavaScript language strategy.

This module validates:
- supported extensions
- comment syntax
- header generation
- header extraction
"""

from pathlib import Path

from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)


def test_javascript_strategy_extensions() -> None:
    """
    Test supported JavaScript extensions.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    assert ".js" in strategy.extensions
    assert ".jsx" in strategy.extensions
    assert ".ts" in strategy.extensions
    assert ".tsx" in strategy.extensions


def test_javascript_comment_prefix() -> None:
    """
    Test JavaScript comment prefix.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    assert strategy.comment_prefix == "//"


def test_javascript_build_header() -> None:
    """
    Test JavaScript header generation.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    header = strategy.build_header(Path("src/main.js"))

    assert header == "// src/main.js"


def test_javascript_extract_valid_header() -> None:
    """
    Test extraction of valid JavaScript header.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    lines = [
        "// src/main.js",
        "",
        'console.log("hello");',
    ]

    header = strategy.extract_header(lines)

    assert header == "// src/main.js"


def test_javascript_extract_missing_header() -> None:
    """
    Test extraction when no header exists.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    lines = [
        'console.log("hello");',
    ]

    header = strategy.extract_header(lines)

    assert header is None


def test_javascript_extract_invalid_comment() -> None:
    """
    Test extraction with unrelated comment.

    Returns:
        None
    """

    strategy = JavaScriptLanguageStrategy()

    lines = [
        "// hello world",
        'console.log("hello");',
    ]

    header = strategy.extract_header(lines)

    assert header == "// hello world"
