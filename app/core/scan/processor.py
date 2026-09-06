# app/core/scan/processor.py

"""
File processing orchestrator.

This module coordinates:
- language strategy resolution
- file analysis
- file updates
- result collection
- summary reporting
"""

import logging
from pathlib import Path

from app.core.scan.updater import FileUpdater
from app.languages.base import BaseLanguageStrategy
from app.models.result import FileProcessResult

logger = logging.getLogger(__name__)


class FileProcessor:
    """
    Orchestrates source file processing.

    This processor:
    - resolves language strategies
    - delegates updates
    - collects results
    - generates summaries
    """

    def __init__(
        self,
        root_directory: Path,
        include_target_directory: bool,
        strategies: list[BaseLanguageStrategy],
    ) -> None:
        """
        Initialize file processor.

        Args:
            root_directory (Path):
                Root project directory.

            strategies (list[BaseLanguageStrategy]):
                Supported language strategies.

        Returns:
            None
        """

        self.root_directory = root_directory
        self.strategies = strategies
        self.include_target_directory = include_target_directory

        self.updater = FileUpdater(
            root_directory=root_directory,
        )

    def process_files(
        self,
        files: list[Path],
        apply_changes: bool = False,
    ) -> list[FileProcessResult]:
        """
        Process multiple source files.

        Args:
            files (list[Path]):
                Files to process.

            apply_changes (bool):
                Whether changes should be written.

        Returns:
            list[FileProcessResult]:
                List of processing results.

        Examples:
            >>> processor.process_files(files)
        """

        results: list[FileProcessResult] = []

        logger.info("[cyan]Processing files...[/cyan]")

        for file_path in files:
            strategy = self._resolve_strategy(
                file_path=file_path,
            )

            if strategy is None:
                continue

            result = self.updater.process_file(
                file_path=file_path,
                strategy=strategy,
                apply_changes=apply_changes,
                include_target_directory=self.include_target_directory,
            )

            results.append(result)

            self._log_result(result)

        return results

    def _resolve_strategy(
        self,
        file_path: Path,
    ) -> BaseLanguageStrategy | None:
        """
        Resolve language strategy for a file.

        Args:
            file_path (Path):
                File path to evaluate.

        Returns:
            BaseLanguageStrategy | None:
                Matching strategy if found,
                otherwise None.
        """

        extension = file_path.suffix.lower()

        for strategy in self.strategies:
            if strategy.supports(extension):
                return strategy

        return None

    def _log_result(
        self,
        result: FileProcessResult,
    ) -> None:
        """
        Log processing result to console.

        Args:
            result (FileProcessResult):
                Processing result object.

        Returns:
            None
        """

        relative_path = result.file_path.relative_to(self.root_directory)

        message = f"{result.icon} {relative_path} ({result.status.value})"

        if result.status.value == "valid":
            logger.debug(message)
        else:
            logger.info(message)
