# tests/unit/config/test_precommit_config.py

from pathlib import Path

import yaml

REQUIRED_REPOS = {
    "https://github.com/astral-sh/ruff-pre-commit",
    "https://github.com/psf/black",
    "https://github.com/pre-commit/pre-commit-hooks",
}


def load_precommit_config() -> dict:
    config_file = Path(".pre-commit-config.yaml")

    assert config_file.exists(), ".pre-commit-config.yaml does not exist"

    return yaml.safe_load(
        config_file.read_text(
            encoding="utf-8",
        )
    )


def test_precommit_config_exists() -> None:
    assert Path(".pre-commit-config.yaml").exists()


def test_precommit_config_is_valid_yaml() -> None:
    config = load_precommit_config()

    assert isinstance(config, dict)


def test_precommit_config_has_repos() -> None:
    config = load_precommit_config()

    assert "repos" in config
    assert isinstance(config["repos"], list)
    assert config["repos"]


def test_required_repositories_exist() -> None:
    config = load_precommit_config()

    repo_urls = {repo["repo"] for repo in config["repos"]}

    missing = REQUIRED_REPOS - repo_urls

    assert not missing, f"Missing required repositories: {missing}"
