# app/languages/html.py

"""
HTML language strategy implementation.

This module contains HTML-specific logic for:
- supported extensions
- comment syntax
- path header detection

Supported file types:
- .html
- .htm
"""

from typing import Optional

from app.languages.base import BaseLanguageStrategy


class HtmlLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation for HTML files.

    Supported extensions:
    - .html
    - .htm

    Features:
    - Uses HTML comments
    - Supports standard HTML documents
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported HTML extensions.

        Returns:
            list[str]:
                Supported HTML extensions.
        """

        return [
            ".html",
            ".htm",
        ]

    @property
    def comment_prefix(self) -> str:
        """
        Return HTML comment prefix.

        Returns:
            str:
                HTML opening comment syntax.
        """

        return "<!--"

    def build_header(self, relative_path) -> str:
        """
        Build HTML-style path header.

        Args:
            relative_path (Path):
                Relative file path from project root.

        Returns:
            str:
                Formatted HTML header string.

        Examples:
            >>> strategy.build_header("templates/index.html")
            '<!-- templates/index.html -->'
        """

        return f"<!-- {relative_path.as_posix()} -->"

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract HTML path header from file content.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found, otherwise None.

        Examples:
            >>> strategy.extract_header(
            ...     ['<!-- templates/index.html -->']
            ... )
            '<!-- templates/index.html -->'
        """

        if not lines:
            return None

        first_line = lines[0].strip()

        if first_line.startswith("<!--") and first_line.endswith("-->"):
            return first_line

        return None
