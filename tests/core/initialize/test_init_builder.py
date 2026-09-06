# tests/core/initialize/test_init_builder.py

"""Tests for initialization spec construction by InitBuilder."""

from pathlib import Path

import pytest

from app.cli.constants.enums import InitMode
from app.core.initialize.builder.init_builder import (
    InitBuilder,
)
from app.core.initialize.models.init_config import (
    InitConfig,
)


def test_build_config_mode_creates_config_spec() -> None:
    """
    Verify CONFIG mode builds a configuration-focused init spec.

    Returns:
        None
    """
    config = InitConfig(mode=InitMode.CONFIG)
    spec = InitBuilder(config).build()

    assert spec.name == "configuration"
    assert len(spec.templates) == 1
    assert ".config/path_header_scanner" in spec.dirs
    assert "✔ Configuration files created" in spec.messages


def test_build_all_mode_includes_all_registered_files() -> None:
    """
    Verify ALL mode includes every currently registered initialization file.

    Returns:
        None
    """
    config = InitConfig(mode=InitMode.ALL)
    spec = InitBuilder(config).build()

    assert spec.name == "all"
    assert len(spec.templates) == 1
    assert spec.templates[0].target_path == Path(
        ".config/path_header_scanner/config.toml"
    )
    assert spec.messages == ["✔ Configuration files created"]


def test_build_raises_for_unsupported_mode() -> None:
    """
    Verify unsupported mode values raise ValueError in builder internals.

    Returns:
        None

    Raises:
        ValueError: Expected when unsupported mode is requested.
    """
    builder = InitBuilder(config=InitConfig(mode=InitMode.ALL))

    with pytest.raises(ValueError, match="Unsupported init mode"):
        builder._build_from_mode("invalid-mode")  # type: ignore[arg-type]
