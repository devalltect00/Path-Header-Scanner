# tests/services/test_banner_service.py

"""Tests for banner rendering and version fallback behavior."""

from app.services.banner_service import BannerService


def test_render_version_uses_get_version(monkeypatch) -> None:
    """
    Verify `render_version` uses `get_version` and prefixes with `v`.

    Args:
        monkeypatch: Pytest fixture to patch service method behavior.

    Returns:
        None
    """
    service = BannerService(package_name="path-header-scanner")

    monkeypatch.setattr(
        service,
        "get_version",
        lambda: "1.2.3",
    )

    assert service.render_version() == "v1.2.3"


def test_get_version_falls_back_when_package_not_found(monkeypatch) -> None:
    """
    Verify `get_version` falls back to local version when package lookup fails.

    Args:
        monkeypatch: Pytest fixture to patch fallback method behavior.

    Returns:
        None
    """
    service = BannerService(package_name="non-existent-package-name-for-test")

    monkeypatch.setattr(
        service,
        "_get_local_version",
        lambda: "0.9.9",
    )

    assert service.get_version() == "0.9.9"


def test_render_banner_returns_non_empty_text() -> None:
    """
    Verify banner rendering returns a non-empty text payload.

    Returns:
        None
    """
    service = BannerService(package_name="path header scanner", font="small")
    banner_text = service.render_banner()

    assert isinstance(banner_text, str)
    assert banner_text.strip() != ""
