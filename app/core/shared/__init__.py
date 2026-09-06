# app/core/shared/__init__.py

"""
Shared core models and utilities.
"""

from .exceptions import (
    ConfigurationError,
    PathHeaderScannerError,
    ValidationError,
)
from .result import CommandResult

__all__ = [
    "CommandResult",
    "PathHeaderScannerError",
    "ConfigurationError",
    "ValidationError",
]
