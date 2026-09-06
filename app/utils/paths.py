# app/utils/paths.py

"""
Path utility helpers.

This module contains reusable helpers for:
- relative path conversion
- normalized path formatting
- safe path display formatting
"""

from pathlib import Path


def to_relative_path(
    file_path: Path,
    root_directory: Path,
) -> Path:
    """
    Convert absolute file path into relative path.

    Args:
        file_path (Path):
            Absolute or full file path.

        root_directory (Path):
            Root project directory.

    Returns:
        Path:
            Relative file path.

    Raises:
        ValueError:
            If file path is not inside root directory.

    Examples:
        >>> to_relative_path(
        ...     Path("/project/app/main.py"),
        ...     Path("/project"),
        ... )
        PosixPath('app/main.py')
    """

    return file_path.relative_to(root_directory)


def normalize_path(path: Path) -> str:
    """
    Normalize path into POSIX-style string.

    This ensures:
    - forward slashes
    - cross-platform consistency

    Args:
        path (Path):
            Path object to normalize.

    Returns:
        str:
            Normalized POSIX-style path string.

    Examples:
        >>> normalize_path(Path("app\\\\main.py"))
        'app/main.py'
    """

    return path.as_posix()


def format_display_path(
    file_path: Path,
    root_directory: Path,
) -> str:
    """
    Format relative path for console display.

    Args:
        file_path (Path):
            Source file path.

        root_directory (Path):
            Root project directory.

    Returns:
        str:
            Relative POSIX-style display path.

    Examples:
        >>> format_display_path(
        ...     Path("/project/app/main.py"),
        ...     Path("/project"),
        ... )
        'app/main.py'
    """

    relative_path = to_relative_path(
        file_path=file_path,
        root_directory=root_directory,
    )

    return normalize_path(relative_path)
