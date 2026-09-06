# app/cli/commands/scan/models.py

from dataclasses import dataclass


@dataclass
class ScanArgs:
    target_directory: str
    workdir: str | None
    apply: bool
    dry_run: bool
    include_target_directory: bool
    debug: bool
