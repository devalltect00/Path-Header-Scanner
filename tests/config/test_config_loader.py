# tests/config/test_config_loader.py

"""Tests for configuration loading, lookups, and resolution precedence."""

from pathlib import Path

import pytest

from app.config.config_loader import ConfigLoader
from app.core.shared import ConfigurationError


def test_config_loader_reads_nested_tool_section(tmp_path: Path) -> None:
    """
    Verify nested `tool.path-header-scanner` sections are read correctly.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.path-header-scanner.logging]
level = "DEBUG"
show_level = true
""".strip(),
        encoding="utf-8",
    )

    loader = ConfigLoader(filename=str(config_file))

    assert loader.get("logging", "level") == "DEBUG"
    assert loader.get("logging", "show_level") is True


def test_config_loader_get_and_get_section_defaults(tmp_path: Path) -> None:
    """
    Verify getter methods return defaults for missing sections/keys.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "empty.toml"
    config_file.write_text("", encoding="utf-8")

    loader = ConfigLoader(filename=str(config_file))

    assert loader.get("missing", default="fallback") == "fallback"
    assert loader.get_section("missing") == {}


def test_config_loader_require_raises_for_missing_key(tmp_path: Path) -> None:
    """
    Verify `require` raises ConfigurationError when a required key is absent.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None

    Raises:
        ConfigurationError: Expected for missing required config key.
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text("", encoding="utf-8")
    loader = ConfigLoader(filename=str(config_file))

    with pytest.raises(ConfigurationError):
        loader.require("cli", "templates", "commit_message")


def test_config_loader_resolve_priority(tmp_path: Path) -> None:
    """
    Verify `resolve` precedence: CLI value > config value > default value.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None
    """
    config_file = tmp_path / "config.toml"
    config_file.write_text(
        """
[tool.path-header-scanner.cli.templates]
commit_message = "from-config.txt"
""".strip(),
        encoding="utf-8",
    )
    loader = ConfigLoader(filename=str(config_file))

    assert (
        loader.resolve(
            cli_value="from-cli.txt",
            config_keys=["cli", "templates", "commit_message"],
            default="default.txt",
        )
        == "from-cli.txt"
    )

    assert (
        loader.resolve(
            cli_value=None,
            config_keys=["cli", "templates", "commit_message"],
            default="default.txt",
        )
        == "from-config.txt"
    )

    assert (
        loader.resolve(
            cli_value=None,
            config_keys=["cli", "templates", "missing"],
            default="default.txt",
        )
        == "default.txt"
    )


def test_config_loader_invalid_toml_raises_configuration_error(
    tmp_path: Path,
) -> None:
    """
    Verify invalid TOML raises ConfigurationError during loader initialization.

    Args:
        tmp_path: Temporary filesystem path fixture.

    Returns:
        None

    Raises:
        ConfigurationError: Expected for invalid TOML syntax.
    """
    config_file = tmp_path / "bad.toml"
    config_file.write_text("[tool.path-header-scanner\ninvalid", encoding="utf-8")

    with pytest.raises(ConfigurationError):
        ConfigLoader(filename=str(config_file))
