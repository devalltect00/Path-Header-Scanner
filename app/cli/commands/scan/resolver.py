# app/cli/commands/scan/resolver.py

from .models import ScanArgs


def resolve_scan_args(config, cli_args) -> ScanArgs:
    dry_run = config.resolve(
        cli_args.dry_run,
        ["cli", "execution", "dry_run"],
        False,
    )
    apply = config.resolve(
        cli_args.apply,
        ["cli", "scan", "apply"],
        False,
    )

    return ScanArgs(
        target_directory=config.resolve(
            cli_args.target_directory,
            ["cli", "scan", "target_directory"],
            None,
        ),
        workdir=config.resolve(
            cli_args.workdir,
            ["cli", "scan", "workdir"],
            None,
        ),
        apply=bool(apply and not dry_run),
        dry_run=dry_run,
        include_target_directory=config.resolve(
            cli_args.include_target_directory,
            ["cli", "scan", "include_target_directory"],
            True,
        ),
        debug=config.resolve(
            cli_args.debug,
            ["cli", "execution", "debug"],
            False,
        ),
    )
