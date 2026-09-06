# app/languages/javascript.py

"""
JavaScript language strategy implementation.

This module contains JavaScript-specific logic for:
- supported extensions
- comment syntax
- path header detection

Supported file types:
- .js
- .jsx
- .ts
- .tsx
"""

from typing import Optional

from app.languages.base import BaseLanguageStrategy


class JavaScriptLanguageStrategy(BaseLanguageStrategy):
    """
    Language strategy implementation for JavaScript
    and TypeScript files.

    Supported extensions:
    - .js
    - .jsx
    - .ts
    - .tsx

    Features:
    - Uses '//' comments
    - Supports React and TypeScript files
    """

    @property
    def extensions(self) -> list[str]:
        """
        Return supported JavaScript-related extensions.

        Returns:
            list[str]:
                Supported extensions.
        """

        return [
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
        ]

    @property
    def comment_prefix(self) -> str:
        """
        Return JavaScript comment prefix.

        Returns:
            str:
                JavaScript comment prefix.
        """

        return "//"

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract JavaScript path header from file content.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found, otherwise None.

        Examples:
            >>> strategy.extract_header(
            ...     ['// src/main.js', '', 'console.log("hi")']
            ... )
            '// src/main.js'
        """

        if not lines:
            return None

        first_line = lines[0].strip()

        if first_line.startswith("// "):
            return first_line

        return None
