# tests/utils/test_logging.py

"""Tests for logging formatter behavior and Rich tag normalization."""

import logging

from app.utils.logging import SeperatorFormatter


def _build_record(message: str) -> logging.LogRecord:
    """
    Build a LogRecord helper instance for formatter-focused assertions.

    Args:
        message: The message payload assigned to the log record.

    Returns:
        logging.LogRecord: Constructed record with INFO level metadata.
    """
    return logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg=message,
        args=(),
        exc_info=None,
    )


def test_separator_formatter_removes_rich_tags() -> None:
    """
    Verify formatter strips Rich markup tags from plain output.

    Returns:
        None
    """
    formatter = SeperatorFormatter("%(message)s")
    record = _build_record("[cyan]Hello[/cyan] [bold]World[/bold]")

    result = formatter.format(record)
    assert result == "Hello World"


def test_separator_formatter_empty_message_becomes_separator() -> None:
    """
    Verify empty formatted messages become default separator lines.

    Returns:
        None
    """
    formatter = SeperatorFormatter("%(message)s")
    record = _build_record("")

    result = formatter.format(record)
    assert result == "-" * 50


def test_separator_formatter_cli_command_gets_title_separator() -> None:
    """
    Verify CLI command titles are rendered with emphasized separators.

    Returns:
        None
    """
    formatter = SeperatorFormatter("%(message)s")
    record = _build_record("[cyan]CLI COMMAND[/cyan] | [dim]scan .[/dim]")

    result = formatter.format(record)

    assert "=" * 50 in result
    assert "CLI COMMAND | scan ." in result
