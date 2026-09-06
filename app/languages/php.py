# app/languages/php.py

"""
PHP language strategy implementation.

This module contains PHP-specific logic for:
- supported extensions
- comment syntax
- PHP opening tag handling
- shebang handling
- path header detection

Supported file types:
- .php
"""

from typing import Optional

from app.languages.base import BaseLanguageStrategy


class PhpLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation for PHP files.

    Supported extensions:
    - .php

    Features:
    - Uses '//' comments
    - Preserves shebang lines
    - Preserves PHP opening tags
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported PHP extensions.

        Returns:
            list[str]:
                Supported PHP extensions.
        """

        return [".php"]

    @property
    def comment_prefix(self) -> str:
        """
        Return PHP comment prefix.

        Returns:
            str:
                PHP single-line comment prefix.
        """

        return "//"

    def get_insertion_index(self, lines: list[str]) -> int:
        """
        Determine safe insertion index for PHP headers.

        This method preserves:
        - shebang lines
        - PHP opening tags

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            int:
                Safe insertion index.

        Examples:
            >>> strategy.get_insertion_index(
            ...     ['<?php', 'echo "Hello";']
            ... )
            1
        """

        index = 0

        if not lines:
            return index

        # Preserve shebang
        if lines[0].startswith("#!"):
            index += 1

        # Preserve PHP opening tag
        if len(lines) > index:
            line = lines[index].strip()

            if line.startswith("<?php"):
                index += 1

        return index

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract PHP path header from file content.

        This method skips:
        - shebang lines
        - PHP opening tags

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found, otherwise None.

        Examples:
            >>> strategy.extract_header(
            ...     ['<?php', '// app/index.php']
            ... )
            '// app/index.php'
        """

        if not lines:
            return None

        index = self.get_insertion_index(lines)

        if len(lines) <= index:
            return None

        line = lines[index].strip()

        if line.startswith("// "):
            return line

        return None
