"""Resolve a PEP 440 package version from a Git worktree description.

Docker excludes ``.git`` from its normal build context, so setuptools-scm
cannot discover a source version while installing Path Header Scanner in an
image. Build workflows resolve the version on the host and pass it through
``PHS_BUILD_VERSION`` without copying repository metadata into an image.
"""

from __future__ import annotations

import logging
import re
import subprocess
from collections.abc import Callable
from pathlib import Path

from packaging.version import InvalidVersion, Version

logger = logging.getLogger(__name__)

DEFAULT_BUILD_VERSION = "0.1.0"
GitRunner = Callable[..., subprocess.CompletedProcess[str]]

_GIT_DESCRIPTION = re.compile(
    r"^(?P<tag>.+)-(?P<distance>\d+)-g(?P<revision>[0-9a-f]+)" r"(?:-dirty)?$",
    flags=re.IGNORECASE,
)


def version_from_git_description(
    description: str,
    *,
    fallback: str = DEFAULT_BUILD_VERSION,
) -> str:
    """Convert ``git describe --long`` output into a PEP 440 version.

    Args:
        description: Git description containing a tag, distance, and revision.
        fallback: Version returned when the description has no usable tag.

    Returns:
        A normalized package version for setuptools-scm's pretend-version
        environment variable.

    Notes:
        SemVer prerelease tags normalize to PEP 440 without changing the tag.
    """

    match = _GIT_DESCRIPTION.fullmatch(description.strip())
    if match is None:
        return fallback

    raw_tag = match.group("tag")
    if len(raw_tag) > 1 and raw_tag[0].lower() == "v" and raw_tag[1].isdigit():
        raw_tag = raw_tag[1:]

    try:
        tagged_version = Version(raw_tag)
    except InvalidVersion:
        logger.warning("Unable to normalize Git tag as a package version: %s", raw_tag)
        return fallback

    distance = int(match.group("distance"))
    if distance == 0:
        return tagged_version.public

    if tagged_version.dev is not None:
        return f"{tagged_version.base_version}.dev{tagged_version.dev + distance}"

    if tagged_version.post is not None:
        return (
            f"{tagged_version.base_version}.post{tagged_version.post + 1}"
            f".dev{distance}"
        )

    return f"{tagged_version.public}.post{distance}"


def resolve_repository_version(
    root: str | Path = ".",
    *,
    fallback: str = DEFAULT_BUILD_VERSION,
    runner: GitRunner = subprocess.run,
) -> str:
    """Resolve a normalized build version from the nearest repository tag.

    Args:
        root: Git worktree used for version discovery.
        fallback: Version returned when Git metadata is unavailable.
        runner: Injectable subprocess runner used by tests.

    Returns:
        A normalized package version or the configured fallback.

    Notes:
        Version discovery is read-only and runs Git with ``shell=False``.
    """

    try:
        result = runner(
            ["git", "describe", "--tags", "--long", "--always"],
            cwd=Path(root),
            check=True,
            capture_output=True,
            text=True,
            shell=False,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        logger.warning("Unable to resolve Git build version: %s", error)
        return fallback

    return version_from_git_description(result.stdout, fallback=fallback)


def main() -> None:
    """Print the current repository version for build workflows."""

    print(resolve_repository_version())


if __name__ == "__main__":
    main()
