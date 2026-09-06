# app/ui/progress.py

"""
Progress utilities.

Provides reusable Rich progress indicators for long-running
operations such as:

- scanning repositories
- generating markdown
- writing files
- analyzing repositories

Example
-------

with progress_spinner("Scanning repository"):
    scan()

with progress_spinner("Generating markdown"):
    build_document()
"""

from contextlib import contextmanager

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
)


@contextmanager
def progress_spinner(
    message: str,
):
    """
    Display a temporary spinner.

    Parameters
    ----------
    message:
        Description displayed beside the spinner.

    Notes
    -----
    The progress indicator automatically disappears when
    the operation completes.
    """

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    )

    with progress:
        task = progress.add_task(
            description=message,
            total=None,
        )

        yield

        progress.update(
            task,
            description=f"{message} ✔",
        )
