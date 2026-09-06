# app/models/result.py

"""
Result models used across the application.

This module contains structured result objects returned
by scanners, analyzers, processors, and updaters.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from app.models.enums import FileStatus


@dataclass
class FileProcessResult:
    """
    Represents the result of processing a single source file.

    This model is used to store information about:
    - file path
    - processing status
    - expected header
    - detected header
    - optional error messages

    Attributes:
        file_path (Path):
            Absolute or relative path to the processed file.

        status (FileStatus):
            Final processing status.

        expected_header (str):
            Expected header value for the file.

        current_header (Optional[str]):
            Currently detected header in the file.

        message (Optional[str]):
            Additional status or error message.
    """

    file_path: Path
    status: FileStatus
    expected_header: str
    current_header: Optional[str] = None
    message: Optional[str] = None

    @property
    def icon(self) -> str:
        """
        Return a display icon based on processing status.

        Returns:
            str:
                Unicode icon representing the result status.

        Examples:
            >>> result.icon
            '✔'
        """

        icon_map = {
            FileStatus.VALID: "✔",
            FileStatus.MISSING: "+",
            FileStatus.INVALID: "~",
            FileStatus.UPDATED: "✔",
            FileStatus.INSERTED: "✔",
            FileStatus.FAILED: "✖",
            FileStatus.SKIPPED: "?",
        }

        return icon_map.get(self.status, "?")
