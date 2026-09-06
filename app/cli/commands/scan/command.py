# app/cli/commands/scan/command.py

"""
This module provides commands for:
- scanning source files
- validating headers
- inserting missing headers
- updating invalid headers
"""

import logging

import typer

from app.cli.constants.args import CliArgs
from app.cli.errors import handle_cli_errors
from app.config.config_loader import get_config
from app.core.scan.processor import FileProcessor
from app.core.scan.scanner import FileScanner
from app.languages.html import HtmlLanguageStrategy
from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)
from app.languages.markdown import (
    MarkdownLanguageStrategy,
)
from app.languages.php import PhpLanguageStrategy
from app.languages.python import (
    PythonLanguageStrategy,
)
from app.languages.shell import ShellLanguageStrategy
from app.ui.console import console
from app.utils.logging import setup_logging
from app.utils.resolver import resolve_target_path

from .options import (
    applyOption,
    debugOption,
    dryRunOption,
    includeTargetDirectoryOption,
    targetDirectoryOption,
    workDirOption,
)
from .resolver import resolve_scan_args

logger = logging.getLogger(__name__)


@handle_cli_errors(
    "Scan",
    solution=(
        "Verify the target and --workdir paths, then retry without --apply or "
        "with --dry-run before approving file changes."
    ),
)
def scan(
    target_directory: targetDirectoryOption = None,
    workdir: workDirOption = None,
    apply: applyOption = None,
    dry_run: dryRunOption = None,
    include_target_directory: includeTargetDirectoryOption = None,
    debug: debugOption = None,
) -> None:
    """
    Scan and process source files.

    This command:
    - scans supported files
    - validates path headers
    - inserts missing headers
    - updates invalid headers

    Args:
        target_directory (str):
            Directory to scan.

        workdir (str | None):
            Optional base working directory
            used to resolve relative paths.

        apply (bool):
            Whether file changes should be written.

        dry_run (bool):
            Simulate scanning without writing, even when apply is configured.

        debug (bool):
            Enable debug logging.

    Returns:
        None

    Examples:
        Scan only (Scan directory without applying changes):

        >>> python -m app.cli.main scan app

        Apply changes:

        >>> python -m app.cli.main scan app --apply

        Use custom working directory:

        >>> python -m app.cli.main scan src \\
        ...     --workdir /workspace/project
    """

    config = get_config()

    # REQUIRED defaults
    cli_args = CliArgs(
        target_directory=target_directory,
        # Options
        workdir=workdir,
        apply=apply,
        dry_run=dry_run,
        include_target_directory=include_target_directory,
        debug=debug,
    )

    args = resolve_scan_args(config=config, cli_args=cli_args)

    setup_logging(debug=args.debug)

    target_path = resolve_target_path(
        target_path=args.target_directory,
        working_directory=args.workdir,
    )

    strategies = [
        PythonLanguageStrategy(),
        JavaScriptLanguageStrategy(),
        ShellLanguageStrategy(),
        HtmlLanguageStrategy(),
        PhpLanguageStrategy(),
        MarkdownLanguageStrategy(),
    ]

    logger.info("")
    logger.info("[bold cyan]PATH HEADER SCANNER[/bold cyan]")
    logger.info("")

    logger.debug(
        "[yellow]Target Directory: %s[/yellow]",
        args.target_directory,
    )

    logger.debug(
        "[yellow]Resolved Path: %s[/yellow]",
        target_path,
    )

    if args.workdir:
        logger.info(
            "Working Directory: %s",
            args.workdir,
        )

    logger.info("")

    scanner = FileScanner(
        root_directory=target_path,
        strategies=strategies,
    )

    files = scanner.scan()

    if not files:
        logger.warning("[yellow]No supported files found[/yellow]")

        raise typer.Exit(code=0)

    processor = FileProcessor(
        root_directory=target_path,
        strategies=strategies,
        include_target_directory=args.include_target_directory,
    )

    results = processor.process_files(
        files=files,
        apply_changes=args.apply,
    )

    logger.info("")
    logger.info("[bold cyan]SUMMARY[/bold cyan]")

    valid_count = sum(1 for result in results if result.status.value == "valid")

    updated_count = sum(1 for result in results if result.status.value == "updated")

    inserted_count = sum(1 for result in results if result.status.value == "inserted")

    failed_count = sum(1 for result in results if result.status.value == "failed")

    logger.info(
        "[green]Valid:[/green] %s",
        valid_count,
    )

    logger.info(
        "[yellow]Updated:[/yellow] %s",
        updated_count,
    )

    logger.info(
        "[cyan]Inserted:[/cyan] %s",
        inserted_count,
    )

    logger.info(
        "[red]Failed:[/red] %s",
        failed_count,
    )

    logger.info("")

    if args.dry_run:
        console.print(
            "[bold yellow]Dry-run mode: no files modified; --apply ignored.[/bold yellow]"
        )
    elif args.apply:
        logger.info("[bold green]Changes applied[/bold green]")
    else:
        logger.info("[bold yellow]Preview mode (no files modified)[/bold yellow]")
