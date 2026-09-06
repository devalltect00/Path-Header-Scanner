# app/ui/tables.py

"""
Reusable Rich tables.

This module contains presentation helpers used
to display structured information to users.

Current tables:

- configuration_table()
"""

from pathlib import Path

from rich.table import Table


def configuration_table(
    *,
    target_directory: Path,
    profile: str,
    smart_mode: bool,
    max_depth: int,
    show_files: bool,
    collapse_dirs: set[str],
    project_type: str | None,
) -> Table:
    """
    Create configuration summary table.

    Parameters
    ----------
    target_directory:
        Repository root directory.

    profile:
        Active profile.

    smart_mode:
        Smart mode status.

    max_depth:
        Maximum traversal depth.

    show_files:
        Include files in tree output.

    collapse_dirs:
        Collapsed directories.

    project_type:
        Forced project type if provided.

    Returns
    -------
    Table
    """

    table = Table(
        title="Configuration",
    )

    table.add_column(
        "Setting",
        style="cyan",
    )

    table.add_column(
        "Value",
    )

    table.add_row(
        "Target Directory",
        str(target_directory),
    )

    table.add_row(
        "Profile",
        str(profile),
    )

    table.add_row(
        "Smart Mode",
        str(smart_mode),
    )

    table.add_row(
        "Max Depth",
        str(max_depth),
    )

    table.add_row(
        "Show Files",
        str(show_files),
    )

    table.add_row(
        "Project Type",
        str(project_type),
    )

    table.add_row(
        "Collapse Directories",
        ", ".join(sorted(collapse_dirs)) if collapse_dirs else "-",
    )

    return table
