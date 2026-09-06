# tests/conftest.py

"""
Shared pytest fixtures and test utilities.

This module contains reusable fixtures used across:
- strategy tests
- updater tests
- scanner tests
- integration tests
"""

from pathlib import Path

import pytest

from app.languages.html import HtmlLanguageStrategy
from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)
from app.languages.php import PhpLanguageStrategy
from app.languages.python import (
    PythonLanguageStrategy,
)
from app.languages.shell import ShellLanguageStrategy


@pytest.fixture
def python_strategy() -> PythonLanguageStrategy:
    """
    Provide Python language strategy instance.

    Returns:
        PythonLanguageStrategy:
            Strategy instance.
    """

    return PythonLanguageStrategy()


@pytest.fixture
def javascript_strategy() -> JavaScriptLanguageStrategy:
    """
    Provide JavaScript language strategy instance.

    Returns:
        JavaScriptLanguageStrategy:
            Strategy instance.
    """

    return JavaScriptLanguageStrategy()


@pytest.fixture
def shell_strategy() -> ShellLanguageStrategy:
    """
    Provide shell language strategy instance.

    Returns:
        ShellLanguageStrategy:
            Strategy instance.
    """

    return ShellLanguageStrategy()


@pytest.fixture
def html_strategy() -> HtmlLanguageStrategy:
    """
    Provide HTML language strategy instance.

    Returns:
        HtmlLanguageStrategy:
            Strategy instance.
    """

    return HtmlLanguageStrategy()


@pytest.fixture
def php_strategy() -> PhpLanguageStrategy:
    """
    Provide PHP language strategy instance.

    Returns:
        PhpLanguageStrategy:
            Strategy instance.
    """

    return PhpLanguageStrategy()


@pytest.fixture
def sample_python_file(
    tmp_path: Path,
) -> Path:
    """
    Create sample Python source file.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        Path:
            Created Python file.
    """

    file_path = tmp_path / "main.py"

    file_path.write_text(
        'print("hello")\n',
        encoding="utf-8",
    )

    return file_path


@pytest.fixture
def sample_javascript_file(
    tmp_path: Path,
) -> Path:
    """
    Create sample JavaScript source file.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        Path:
            Created JavaScript file.
    """

    file_path = tmp_path / "main.js"

    file_path.write_text(
        'console.log("hello");\n',
        encoding="utf-8",
    )

    return file_path
