# app/languages/base.py

"""
Base language strategy definitions.

This module defines the abstract interface used by all
language-specific handlers.

Each language strategy is responsible for:
- determining supported extensions
- generating file headers
- detecting existing headers
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class BaseLanguageStrategy(ABC):
    """
    Base strategy for language-specific file handling.

    Subclasses implement:
    - supported file extensions
    - comment syntax
    - header generation
    - header detection logic
    """

    @property
    @abstractmethod
    def extensions(self) -> list[str]:
        """
        Return supported file extensions.

        Returns:
            list[str]:
                List of supported extensions.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def comment_prefix(self) -> str:
        """
        Return language comment prefix.

        Returns:
            str:
                Comment prefix used for headers.
        """
        raise NotImplementedError

    def supports(self, extension: str) -> bool:
        """
        Check whether the strategy supports a file extension.

        Args:
            extension (str):
                File extension including leading dot.

        Returns:
            bool:
                True if supported, otherwise False.

        Examples:
            >>> strategy.supports(".py")
            True
        """

        return extension.lower() in self.extensions

    def build_header(self, relative_path: Path) -> str:
        """
        Build the expected header string.

        Args:
            relative_path (Path):
                Relative file path from project root.

        Returns:
            str:
                Formatted header string.

        Examples:
            >>> strategy.build_header(Path("app/core/main.py"))
            '# app/core/main.py'
        """

        return f"{self.comment_prefix} {relative_path.as_posix()}"

    def extract_header(self, lines: list[str]) -> Optional[str]:
        """
        Extract header from file content.

        This method checks the first meaningful line
        and determines whether it looks like a path header.

        Args:
            lines (list[str]):
                File content split into lines.

        Returns:
            Optional[str]:
                Detected header if found, otherwise None.
        """

        if not lines:
            return None

        first_line = lines[0].strip()

        if first_line.startswith(self.comment_prefix):
            return first_line

        return None
