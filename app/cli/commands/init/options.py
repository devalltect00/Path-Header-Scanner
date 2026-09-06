# app/cli/commands/init/options.py

from typing import Annotated

import typer

from app.cli.constants.completions import completion_initialization_mode
from app.cli.constants.enums import (
    InitMode,
)

# =========================================================
# 🟢 INITIALIZATION OPTIONS
# =========================================================
ModeOption = Annotated[
    InitMode,
    typer.Option(
        ...,
        "--mode",
        "-m",
        help="""
        [bold]Initialization Mode[/bold]

        [bold yellow]•[/bold yellow] [bold]all[/bold]             [yellow]→[/yellow] initialize all. ([dim]e.i.[/dim] config, version, templates, examples files)\n
        [bold yellow]•[/bold yellow] [bold]all_no_examples[/bold] [yellow]→[/yellow] initialize all except examples. ([dim]e.i.[/dim] config, version, templates files)\n
        [bold yellow]•[/bold yellow] [bold]config[/bold]          [yellow]→[/yellow] initialize config.\n
        [bold yellow]•[/bold yellow] [bold]templates[/bold]       [yellow]→[/yellow] initialize templates\n
        [bold yellow]•[/bold yellow] [bold]examples[/bold]        [yellow]→[/yellow] initialize examples

        [dim bright_green]SUGGESTION:[/dim bright_green] all.
        [dim yellow]HINT:[/dim yellow] Recommended when installing or running the application for the first time.
        """,
        rich_help_panel="Initialization • Executions",
        autocompletion=completion_initialization_mode,
        case_sensitive=False,
    ),
]
ForceOption = Annotated[
    bool,
    typer.Option(
        "--force/--no-force",
        "-f/-F",
        help="""
        [bold red]Force initialization[/bold red]

        Force to initialization and overwrite existing files and folders
        """,
        rich_help_panel="Initialization • Behavior",
    ),
]
AskOption = Annotated[
    bool,
    typer.Option(
        "--ask",
        "-a",
        help="""
        [bold red]Asking to Initialization[/bold red]

        Ask user to initialization and overwrite existing files and folders
        """,
        rich_help_panel="Initialization • Behavior",
    ),
]

# ---------------------------
# EXECUTION OPTIONS
# ---------------------------
DryRunOption = Annotated[
    bool,
    typer.Option(
        "--dry-run/--no-dry-run",
        "-dr/-Dr",
        help="""
        [bold yellow]Dry run mode[/bold yellow]

        Preview initialization without creating directories, writing files,
        overwriting content, or prompting for confirmation.

        [dim yellow]HINT:[/dim yellow] Useful for debugging
        """,
        rich_help_panel="CLI and Execution Options",
    ),
]
