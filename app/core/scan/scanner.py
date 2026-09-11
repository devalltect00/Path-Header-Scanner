# app/core/scan/scanner.py

"""
File scanning utilities.

This module is responsible for:
- recursively scanning directories
- filtering supported source files
- skipping ignored directories
- matching files against language strategies
"""

import logging
from pathlib import Path

from app.languages.base import BaseLanguageStrategy

logger = logging.getLogger(__name__)


class FileScanner:
    """
    Recursively scan directories for supported source files.

    This scanner:
    - walks through directories
    - filters supported extensions
    - skips ignored directories
    - returns matching source files
    """

    DEFAULT_IGNORED_DIRECTORIES = {
        ".git",
        ".venv",
        "venv",
        "dev_venv",
        "prod_venv",
        "venv_dev",
        "venv_prod",
        "publish_venv",
        "venv_publish",
        "other_venv",
        "venv_other",
        "__pycache__",
        "node_modules",
        "dist",
        "build",
    }

    def __init__(
        self,
        root_directory: Path,
        strategies: list[BaseLanguageStrategy],
        ignored_directories: set[str] | None = None,
    ) -> None:
        """
        Initialize file scanner.

        Args:
            root_directory (Path):
                Root directory to scan.

            strategies (list[BaseLanguageStrategy]):
                Supported language strategies.

            ignored_directories (set[str] | None):
                Optional custom ignored directories.

        Returns:
            None
        """

        self.root_directory = root_directory
        self.strategies = strategies

        self.ignored_directories = (
            ignored_directories or self.DEFAULT_IGNORED_DIRECTORIES
        )

    def scan(self) -> list[Path]:
        """
        Scan directory recursively for supported files.

        Returns:
            list[Path]:
                List of discovered source files.

        Raises:
            FileNotFoundError:
                If root directory does not exist.

        Examples:
            >>> scanner.scan()
            [PosixPath('app/main.py')]
        """

        logger.debug(
            "[cyan]Scanning directory:[/cyan] %s",
            self.root_directory,
        )

        logger.debug(
            "[yellow]Runtime Path:[/yellow] %s",
            self.root_directory.resolve(),
        )

        logger.info(
            "[yellow]Scanning directory:[/yellow] %s",
            self.root_directory.name,
        )

        if not self.root_directory.exists():
            raise FileNotFoundError(f"Directory does not exist: {self.root_directory}")

        matched_files: list[Path] = []

        for file_path in self.root_directory.rglob("*"):
            if not file_path.is_file():
                continue

            if self._is_ignored(file_path):
                continue

            if self._is_supported(file_path):
                matched_files.append(file_path)

        logger.info(
            "[green]Found %s supported files[/green]",
            len(matched_files),
        )

        return sorted(matched_files)

    def _is_ignored(self, file_path: Path) -> bool:
        """
        Check whether file path should be ignored.

        Args:
            file_path (Path):
                File path to evaluate.

        Returns:
            bool:
                True if ignored, otherwise False.
        """

        return any(part in self.ignored_directories for part in file_path.parts)

    def _is_supported(self, file_path: Path) -> bool:
        """
        Check whether file is supported by any strategy.

        Args:
            file_path (Path):
                File path to evaluate.

        Returns:
            bool:
                True if supported, otherwise False.
        """

        extension = file_path.suffix.lower()

        return any(strategy.supports(extension) for strategy in self.strategies)
