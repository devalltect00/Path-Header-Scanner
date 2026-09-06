# app/languages/python.py

"""
Python language strategy implementation.

This module contains Python-specific logic for:
- supported extensions
- comment syntax
- shebang handling
- encoding header handling
- path header detection
"""

from typing import Optional

from app.languages.base import BaseLanguageStrategy


class PythonLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation for Python files.

    Supported extensions:
    - .py

    Features:
    - Uses '#' comments
    - Preserves shebang lines
    - Preserves encoding declarations
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported Python extensions.

        Returns:
            list[str]:
                Supported Python extensions.
        """

        return [".py"]

    @property
    def comment_prefix(self) -> str:
        """
        Return Python comment prefix.

        Returns:
            str:
                Python comment prefix.
        """

        return "#"

    def get_insertion_index(self, lines: list[str]) -> int:
        """
        Determine safe insertion index for headers.

        This method preserves:
        - shebang lines
        - encoding declarations

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            int:
                Safe insertion index.

        Examples:
            >>> strategy.get_insertion_index(
            ...     ['#!/usr/bin/env python3', 'print("hi")']
            ... )
            1
        """

        index = 0

        if not lines:
            return index

        # Preserve shebang
        if lines[0].startswith("#!"):
            index += 1

        # Preserve encoding declaration
        if len(lines) > index:
            encoding_line = lines[index]

            if "coding" in encoding_line:
                index += 1

        return index

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract Python path header from file content.

        This method skips:
        - shebang lines
        - encoding declarations

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
