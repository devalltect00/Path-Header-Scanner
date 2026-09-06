# app/languages/markdown.py

"""
Markdown language strategy implementation.

This module contains Markdown-specific logic for:
- supported extensions
- HTML comment syntax
- path header detection

Supported file types:
- .md
- .markdown
"""

import re
from typing import Optional

from app.languages.base import BaseLanguageStrategy

PATH_PATTERN = re.compile(r"^#\s+[\w./-]+\.[a-zA-Z0-9]+$")


class MarkdownLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation
    for Markdown files.

    Supported extensions:
    - .md
    - .markdown

    Features:
    - Uses HTML comments
    - Avoids conflict with Markdown headings
    - GitHub-compatible
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported Markdown extensions.

        Returns:
            list[str]:
                Supported Markdown extensions.
        """

        return [
            ".md",
            ".markdown",
        ]

    @property
    def comment_prefix(self) -> str:
        """
        Return Markdown comment prefix.

        Returns:
            str:
                HTML comment syntax.
        """

        return "<!--"

    def build_header(
        self,
        relative_path,
    ) -> str:
        """
        Build Markdown path header.

        Args:
            relative_path (Path):
                Relative file path.

        Returns:
            str:
                Formatted Markdown header.
        """

        return f"<!-- {relative_path.as_posix()} -->"

    def extract_header(
        self,
        lines: list[str],
    ) -> Optional[str]:
        """
        Extract Markdown path header.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found.
        """

        if not lines:
            return None

        first_line = lines[0].strip()

        # =====================================
        # HTML COMMENT HEADER
        # =====================================
        if first_line.startswith("<!--") and first_line.endswith("-->"):
            return first_line

        # =====================================
        # LEGACY MARKDOWN HEADER
        # =====================================

        if PATH_PATTERN.match(first_line):
            return first_line

        return None
