# app/core/scan/updater.py

"""
File update utilities.

This module is responsible for:
- inserting missing headers
- replacing invalid headers
- preserving special lines
- rebuilding file content safely
"""

import logging
from pathlib import Path

from app.languages.base import BaseLanguageStrategy
from app.models.enums import FileStatus
from app.models.result import FileProcessResult

logger = logging.getLogger(__name__)


class FileUpdater:
    """
    Update source file headers safely.

    This updater:
    - inserts missing headers
    - replaces invalid headers
    - preserves shebangs and special lines
    - avoids unnecessary rewrites
    """

    def __init__(
        self,
        root_directory: Path,
    ) -> None:
        """
        Initialize file updater.

        Args:
            root_directory (Path):
                Root project directory.

        Returns:
            None
        """

        self.root_directory = root_directory

    def process_file(
        self,
        file_path: Path,
        strategy: BaseLanguageStrategy,
        apply_changes: bool = False,
        include_target_directory: bool = True,
    ) -> FileProcessResult:
        """
        Process a single source file.

        Args:
            file_path (Path):
                File to process.

            strategy (BaseLanguageStrategy):
                Language strategy for the file.

            apply_changes (bool):
                Whether changes should be written.

            include_target_directory (bool):
                Whether to include the target directory in generated headers.

        Returns:
            FileProcessResult:
                Processing result object.

        Raises:
            RuntimeError:
                If file processing fails.
        """

        try:
            # Determine relative path for header generation
            if include_target_directory:
                relative_path = file_path.relative_to(self.root_directory.parent)
            else:
                relative_path = file_path.relative_to(self.root_directory)

            expected_header = strategy.build_header(relative_path)

            content = file_path.read_text(encoding="utf-8")

            lines = content.splitlines()

            current_header = strategy.extract_header(lines)

            # =========================
            # VALID
            # =========================
            if current_header == expected_header:
                return FileProcessResult(
                    file_path=file_path,
                    status=FileStatus.VALID,
                    expected_header=expected_header,
                    current_header=current_header,
                    message="Header already valid",
                )

            # =========================
            # INVALID
            # =========================
            if current_header is not None:
                updated_content = self._replace_header(
                    lines=lines,
                    strategy=strategy,
                    new_header=expected_header,
                )

                if apply_changes:
                    file_path.write_text(
                        updated_content,
                        encoding="utf-8",
                    )

                    logger.info(
                        "[yellow]Updated:[/yellow] %s",
                        relative_path,
                    )

                return FileProcessResult(
                    file_path=file_path,
                    status=FileStatus.UPDATED,
                    expected_header=expected_header,
                    current_header=current_header,
                    message="Header updated",
                )

            # =========================
            # MISSING
            # =========================
            updated_content = self._insert_header(
                lines=lines,
                strategy=strategy,
                new_header=expected_header,
            )

            if apply_changes:
                file_path.write_text(
                    updated_content,
                    encoding="utf-8",
                )

                logger.info(
                    "[green]Inserted:[/green] %s",
                    relative_path,
                )

            return FileProcessResult(
                file_path=file_path,
                status=FileStatus.INSERTED,
                expected_header=expected_header,
                current_header=current_header,
                message="Header inserted",
            )

        except Exception as error:
            logger.exception(
                "Failed processing file: %s",
                file_path,
            )

            return FileProcessResult(
                file_path=file_path,
                status=FileStatus.FAILED,
                expected_header="",
                current_header=None,
                message=str(error),
            )

    def _replace_header(
        self,
        lines: list[str],
        strategy: BaseLanguageStrategy,
        new_header: str,
    ) -> str:
        """
        Replace existing invalid header.

        Args:
            lines (list[str]):
                Original file lines.

            strategy (BaseLanguageStrategy):
                File language strategy.

            new_header (str):
                Replacement header.

        Returns:
            str:
                Updated file content.
        """

        insertion_index = self._get_insertion_index(
            strategy,
            lines,
        )

        lines[insertion_index] = new_header

        return "\n".join(lines) + "\n"

    def _insert_header(
        self,
        lines: list[str],
        strategy: BaseLanguageStrategy,
        new_header: str,
    ) -> str:
        """
        Insert missing header into file.

        Args:
            lines (list[str]):
                Original file lines.

            strategy (BaseLanguageStrategy):
                File language strategy.

            new_header (str):
                Header to insert.

        Returns:
            str:
                Updated file content.
        """

        insertion_index = self._get_insertion_index(
            strategy,
            lines,
        )

        updated_lines = list(lines)

        updated_lines.insert(
            insertion_index,
            new_header,
        )

        has_content = any(line.strip() for line in lines)

        if has_content:
            updated_lines.insert(
                insertion_index + 1,
                "",
            )

        return "\n".join(updated_lines) + "\n"

    def _get_insertion_index(
        self,
        strategy: BaseLanguageStrategy,
        lines: list[str],
    ) -> int:
        """
        Determine insertion index using strategy logic.

        Args:
            strategy (BaseLanguageStrategy):
                File language strategy.

            lines (list[str]):
                File content split into lines.

        Returns:
            int:
                Safe insertion index.
        """

        if hasattr(strategy, "get_insertion_index"):
            return strategy.get_insertion_index(lines)

        return 0
