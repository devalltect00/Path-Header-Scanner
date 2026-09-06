# app/models/enums.py

"""
Enum definitions used across the application.

This module centralizes processing states and file analysis
results used by scanners, processors, and updaters.
"""

from enum import StrEnum


class FileStatus(StrEnum):
    """
    Represents processing status for source files.

    These statuses are used during scanning, validation,
    updating, and reporting.

    Attributes:
        VALID:
            File already contains the correct header.

        MISSING:
            File does not contain a header.

        INVALID:
            File contains an incorrect header.

        UPDATED:
            File header was successfully updated.

        INSERTED:
            File header was successfully inserted.

        FAILED:
            File processing failed.

        SKIPPED:
            File was intentionally skipped.
    """

    VALID = "valid"
    MISSING = "missing"
    INVALID = "invalid"
    UPDATED = "updated"
    INSERTED = "inserted"
    FAILED = "failed"
    SKIPPED = "skipped"
