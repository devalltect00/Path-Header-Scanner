# app/cli/utils/versions.py

import typer
import typer.rich_utils
from rich import print as rprint

from app.services.banner_service import BannerService
from app.theme import theme

banner = BannerService(package_name="PATH HEADER SCANNER", font="small")


def get_version():
    __version__ = banner.get_version()
    return __version__


def version_callback(value: bool):
    if value:
        __version__ = banner.get_version()
        rprint(
            f"[{theme.primary}]Path Header Scanner[/{theme.primary}]: [{theme.secondary}]{__version__}[/{theme.secondary}]"
        )
        raise typer.Exit()
