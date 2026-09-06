# tests/languages/test_html_strategy.py

"""
Tests for HTML language strategy.

This module validates:
- supported extensions
- comment syntax
- header generation
- header extraction
"""

from pathlib import Path

from app.languages.html import (
    HtmlLanguageStrategy,
)


def test_html_strategy_extensions() -> None:
    """
    Test supported HTML extensions.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    assert ".html" in strategy.extensions
    assert ".htm" in strategy.extensions


def test_html_comment_prefix() -> None:
    """
    Test HTML comment prefix.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    assert strategy.comment_prefix == "<!--"


def test_html_build_header() -> None:
    """
    Test HTML header generation.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    header = strategy.build_header(Path("templates/index.html"))

    assert header == "<!-- templates/index.html -->"


def test_html_extract_valid_header() -> None:
    """
    Test extraction of valid HTML header.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    lines = [
        "<!-- templates/index.html -->",
        "",
        "<html></html>",
    ]

    header = strategy.extract_header(lines)

    assert header == "<!-- templates/index.html -->"


def test_html_extract_missing_header() -> None:
    """
    Test extraction when no header exists.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    lines = [
        "<html></html>",
    ]

    header = strategy.extract_header(lines)

    assert header is None


def test_html_extract_invalid_comment() -> None:
    """
    Test extraction with unrelated HTML comment.

    Returns:
        None
    """

    strategy = HtmlLanguageStrategy()

    lines = [
        "<!-- hello world -->",
        "<html></html>",
    ]

    header = strategy.extract_header(lines)

    assert header == "<!-- hello world -->"
