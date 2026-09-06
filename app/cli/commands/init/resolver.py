# app/cli/commands/init/resolver.py

from app.cli.constants.enums import (
    InitMode,
)

from .models import InitArgs


def resolve_init_args(config, cli_args) -> InitArgs:
    return InitArgs(
        mode=cli_args.mode or InitMode.ALL,
        force_init=config.resolve(
            cli_args.force_init,
            ["initialization", "force"],
            False,
        ),
        ask=config.resolve(
            cli_args.ask,
            ["initialization", "ask"],
            False,
        ),
        dry_run=config.resolve(
            cli_args.dry_run,
            ["cli", "execution", "dry_run"],
            False,
        ),
    )
