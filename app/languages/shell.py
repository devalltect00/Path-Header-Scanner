# app/languages/shell.py

"""
Shell language strategy implementation.

This module contains shell-specific logic for:
- supported extensions
- comment syntax
- shebang handling
- path header detection

Supported file types:
- .sh
- .bash
- .zsh
"""

from typing import Optional

from app.languages.base import BaseLanguageStrategy


class ShellLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation for shell scripts.

    Supported extensions:
    - .sh
    - .bash
    - .zsh

    Features:
    - Uses '#' comments
    - Preserves shebang lines
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported shell extensions.

        Returns:
            list[str]:
                Supported shell script extensions.
        """

        return [
            ".sh",
            ".bash",
            ".zsh",
        ]

    @property
    def comment_prefix(self) -> str:
        """
        Return shell comment prefix.

        Returns:
            str:
                Shell comment prefix.
        """

        return "#"

    def get_insertion_index(self, lines: list[str]) -> int:
        """
        Determine safe insertion index for shell headers.

        This method preserves shebang lines.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            int:
                Safe insertion index.

        Examples:
            >>> strategy.get_insertion_index(
            ...     ['#!/bin/bash', 'echo hello']
            ... )
            1
        """

        if not lines:
            return 0

        if lines[0].startswith("#!"):
            return 1

        return 0

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract shell path header from file content.

        This method skips shebang lines before checking
        for a path header.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found, otherwise None.
        """

        if not lines:
            return None

        index = self.get_insertion_index(lines)

        if len(lines) <= index:
            return None

        line = lines[index].strip()

        if line.startswith("# "):
            return line

        return None
