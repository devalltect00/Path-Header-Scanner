# app/cli/errors.py

"""Reusable exception boundaries for user-facing CLI commands."""

from __future__ import annotations

import logging
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

import typer
from click.exceptions import Abort, ClickException, Exit

from app.core.shared import PathHeaderScannerError
from app.ui.exceptions import show_error

logger = logging.getLogger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


def handle_cli_errors(
    operation: str,
    *,
    solution: str | None = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Convert expected and unexpected failures into concise CLI errors."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return func(*args, **kwargs)
            except (Exit, Abort, ClickException, typer.Exit, typer.Abort):
                raise
            except (PathHeaderScannerError, OSError) as exc:
                logger.debug("%s failed: %s", operation, exc, exc_info=True)
                message = f"{operation} failed\n\n{exc}"
                if solution:
                    message += f"\n\nSolution\n\n{solution}"
                show_error(message)
                raise typer.Exit(code=1) from None
            except Exception as exc:
                logger.debug(
                    "%s failed unexpectedly: %s", operation, exc, exc_info=True
                )
                show_error(
                    f"{operation} failed unexpectedly.\n\n"
                    "Re-run with --debug when supported and inspect the "
                    "configured log file for technical details."
                )
                raise typer.Exit(code=1) from None

        return wrapper

    return decorator
