"""Tests for container build-version resolution."""

from __future__ import annotations

import subprocess
from pathlib import Path
from unittest.mock import MagicMock

from app.core.build.version import (
    resolve_repository_version,
    version_from_git_description,
)


def test_exact_semver_release() -> None:
    """An exact prefixed SemVer tag becomes its public package version."""

    assert version_from_git_description("v1.0.0-0-gabc1234") == "1.0.0"


def test_semver_prerelease_is_normalized_for_python() -> None:
    """SemVer RC spelling converts to a valid PEP 440 package version."""

    assert version_from_git_description("v1.0.0-rc.1-0-gabc1234") == "1.0.0rc1"


def test_commit_distance_and_fallback() -> None:
    """Commit distance is preserved and revision-only input uses fallback."""

    assert version_from_git_description("v1.0.0-3-gabc1234") == "1.0.0.post3"
    assert version_from_git_description("abc1234", fallback="0.0.0") == "0.0.0"


def test_resolver_runs_git_without_a_shell(tmp_path: Path) -> None:
    """Repository discovery uses an argument list and ``shell=False``."""

    runner = MagicMock(
        return_value=subprocess.CompletedProcess(
            args=["git", "describe"],
            returncode=0,
            stdout="v1.0.0-rc.1-0-gabc1234\n",
            stderr="",
        )
    )

    assert resolve_repository_version(tmp_path, runner=runner) == "1.0.0rc1"
    runner.assert_called_once_with(
        ["git", "describe", "--tags", "--long", "--always"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
        shell=False,
    )


def test_resolver_uses_fallback_when_git_is_unavailable(tmp_path: Path) -> None:
    """Unavailable Git metadata returns the explicit fallback."""

    runner = MagicMock(side_effect=FileNotFoundError("git missing"))

    assert (
        resolve_repository_version(tmp_path, fallback="0.0.0", runner=runner) == "0.0.0"
    )
