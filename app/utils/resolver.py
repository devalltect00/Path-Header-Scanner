# app/utils/resolver.py

"""
Project path resolution utilities.

This module provides smart path resolution for:
- local execution
- Docker execution
- mounted workspace environments
- custom working directory support

Features:
- resolves relative paths safely
- supports Docker workspace fallback
- supports explicit working directory
- normalizes final paths
- provides clean error handling
"""

from pathlib import Path

from app.constants.docker import DOCKER_WORKSPACE


def is_running_in_docker() -> bool:
    """
    Detect whether application is running inside Docker.

    Returns:
        bool:
            True if running inside Docker,
            otherwise False.

    Examples:
        >>> is_running_in_docker()
        True
    """

    return Path("/.dockerenv").exists()


def resolve_target_path(
    target_path: str,
    working_directory: str | Path | None = None,
) -> Path:
    """
    Resolve scan target path intelligently.

    Resolution order:
    1. Absolute path
    2. Working directory (if provided)
    3. Docker workspace fallback
    4. Current working directory
    5. Direct relative path

    Args:
        target_path (str):
            Target directory or file path.

        working_directory (
            str | Path | None
        ):
            Optional base working directory
            used to resolve relative paths.

    Returns:
        Path:
            Resolved absolute path.

    Raises:
        FileNotFoundError:
            If target path does not exist.

    Examples:
        Basic usage:

        >>> resolve_target_path("app")
        WindowsPath(
            'E:/project/path_header_scanner/app'
        )

        Using working directory:

        >>> resolve_target_path(
        ...     "src",
        ...     working_directory="/workspace/project",
        ... )
        PosixPath('/workspace/project/src')

        Docker execution:

        >>> resolve_target_path("app")
        PosixPath('/workspace/app')
    """

    input_path = Path(target_path)

    attempted_paths: list[str] = []

    # =====================================================
    # ABSOLUTE PATH
    # =====================================================

    if input_path.is_absolute():
        attempted_paths.append(str(input_path))

        if input_path.exists():
            return input_path.resolve()

    # =====================================================
    # WORKING DIRECTORY
    # =====================================================

    if working_directory is not None:
        workdir_path = Path(working_directory)

        resolved_workdir_path = workdir_path / input_path

        attempted_paths.append(str(resolved_workdir_path))

        if resolved_workdir_path.exists():
            return resolved_workdir_path.resolve()

    # =====================================================
    # DOCKER WORKSPACE FALLBACK
    # =====================================================

    if is_running_in_docker():
        docker_workspace_path = DOCKER_WORKSPACE / input_path

        attempted_paths.append(str(docker_workspace_path))

        if docker_workspace_path.exists():
            return docker_workspace_path.resolve()

    # =====================================================
    # CURRENT WORKING DIRECTORY
    # =====================================================

    cwd_path = Path.cwd() / input_path

    attempted_paths.append(str(cwd_path))

    if cwd_path.exists():
        return cwd_path.resolve()

    # =====================================================
    # DIRECT RELATIVE PATH
    # =====================================================

    attempted_paths.append(str(input_path))

    if input_path.exists():
        return input_path.resolve()

    # =====================================================
    # NOT FOUND
    # =====================================================

    attempted_text = "\n".join(f" - {path}" for path in attempted_paths)

    raise FileNotFoundError(
        "Target path does not exist.\n\n"
        f"Input Path:\n"
        f" - {target_path}\n\n"
        f"Attempted Locations:\n"
        f"{attempted_text}"
    )
