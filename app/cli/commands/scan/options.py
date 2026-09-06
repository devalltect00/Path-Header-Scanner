# app/cli/commands/scan/options.py

from typing import Annotated

import typer

from app.cli.constants.completions import (
    completion_target_directory,
)

# ---------------------------
# EXECUTION OPTIONS
# ---------------------------

targetDirectoryOption = Annotated[
    str,
    typer.Argument(
        ...,
        help="Directory to scan.",
        autocompletion=completion_target_directory,
    ),
]
workDirOption = Annotated[
    str | None,
    typer.Option(
        "--workdir",
        help=("Base working directory used to resolve relative paths."),
    ),
]
applyOption = Annotated[
    bool,
    typer.Option(
        "--apply",
        help="Write changes to files.",
    ),
]
dryRunOption = Annotated[
    bool,
    typer.Option(
        "--dry-run/--no-dry-run",
        "-dr/-Dr",
        help=(
            "Simulate scanning without writing files. Dry-run overrides "
            "--apply and configured apply mode."
        ),
    ),
]
includeTargetDirectoryOption = Annotated[
    bool,
    typer.Option(
        "--include-target-directory/--exclude-target-directory",
        help=("Include the target directory in generated headers."),
    ),
]
debugOption = Annotated[
    bool,
    typer.Option(
        "--debug",
        help="Enable debug logging.",
    ),
]
