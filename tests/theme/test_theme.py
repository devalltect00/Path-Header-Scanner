# tests/theme/test_theme.py

"""Tests for theme loading and Rich theme conversion behavior."""

from app.theme.theme import Theme, load_theme


def test_load_theme_uses_environment_overrides(monkeypatch) -> None:
    """
    Verify environment variables override default theme configuration values.

    Args:
        monkeypatch: Pytest fixture for environment variable patching.

    Returns:
        None
    """
    monkeypatch.setenv("PATH_HEADER_SCANNER_PRIMARY", "#FFFFFF")
    monkeypatch.setenv("PATH_HEADER_SCANNER_SECONDARY", "#000000")
    monkeypatch.setenv("PATH_HEADER_SCANNER_INFO", "blue")

    theme = load_theme()

    assert theme.primary == "#FFFFFF"
    assert theme.secondary == "#000000"
    assert theme.info == "blue"


def test_to_rich_theme_contains_expected_styles() -> None:
    """
    Verify generated Rich theme contains expected named style entries.

    Returns:
        None
    """
    theme = Theme(
        primary="cyan",
        secondary="white",
        info="cyan",
        warning="yellow",
        success="green",
        error="red",
        dry_run="magenta",
        pointing="yellow",
        help_title="cyan",
        help_text="white",
        help_hint="bright_black",
        help_option="cyan",
        help_example="green",
        progress_title="cyan",
        progress_step="yellow",
        progress_done="green",
        center=50,
    )

    rich_theme = theme.to_rich_theme()

    assert "primary" in rich_theme.styles
    assert "help.title" in rich_theme.styles
    assert "progress.done" in rich_theme.styles
