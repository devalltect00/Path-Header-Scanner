# app/core/shared/exceptions.py

"""
Shared exceptions used by Path-Header-Scanner.

This module contains application-specific exceptions used
throughout the project.

Using dedicated exception types makes error handling,
testing, and debugging easier.
"""


class PathHeaderScannerError(Exception):
    """
    Base exception for Path-Header-Scanner.

    All custom Path-Header-Scanner exceptions should inherit from this
    exception.
    """


# =====================================================
# Configuration
# =====================================================


class ConfigurationError(PathHeaderScannerError):
    """
    Raised when configuration is invalid.
    """


# =====================================================
# Validation
# =====================================================


class ValidationError(PathHeaderScannerError):
    """
    Raised when validation fails.
    """
