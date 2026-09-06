# tests/utils/test_parsing.py

"""Tests for size string parsing into byte values."""

from app.utils.parsing import parse_size


def test_parse_size_with_kb() -> None:
    """
    Verify kilobyte unit input is converted to bytes.

    Returns:
        None
    """
    assert parse_size("1KB") == 1024


def test_parse_size_with_mb_decimal() -> None:
    """
    Verify decimal megabyte input is converted using binary base (1024).

    Returns:
        None
    """
    assert parse_size("1.5MB") == int(1.5 * 1024 * 1024)


def test_parse_size_with_gb_spaces_and_case() -> None:
    """
    Verify parser handles surrounding whitespace and lowercase unit casing.

    Returns:
        None
    """
    assert parse_size(" 2gb ") == 2 * 1024 * 1024 * 1024


def test_parse_size_raw_integer_string() -> None:
    """
    Verify raw integer strings are interpreted directly as byte counts.

    Returns:
        None
    """
    assert parse_size("2048") == 2048
