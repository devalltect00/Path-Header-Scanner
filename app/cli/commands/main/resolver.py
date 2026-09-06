# app/cli/commands/main/resolver.py

from .models import MainArgs


def resolve_main_args(config, cli_args) -> MainArgs:
    return MainArgs(
        no_banner=cli_args.no_banner or False,
        help=cli_args.help or False,
        version=cli_args.version or None,
    )
