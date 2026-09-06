# app/cli/commands/main/models.py

from dataclasses import dataclass


@dataclass
class MainArgs:
    no_banner: bool
    help: bool
    version: bool | None
