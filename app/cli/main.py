# app/cli/main.py

"""
Main CLI application.

Entrypoint for Path-Header-Scanner utility.
"""

import typer

from app.ui.console import console

from .commands import (
    init_command,
    main_command,
    scan_command,
)

typer.rich_utils._console = console

app = typer.Typer(
    help="Source file path header utility.",
    add_help_option=False,
    add_completion=True,
    rich_markup_mode="rich",
    pretty_exceptions_enable=True,
)


app.callback(invoke_without_command=True)(main_command.main)

app.command()(init_command.init)
app.command()(scan_command.scan)

if __name__ == "__main__":
    app()
