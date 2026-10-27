"""Settings loaded from .env and config/*.yaml."""

from functools import lru_cache
from pathlib import Path

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", extra="ignore")

    sec_user_agent: str = "IPO-watch contact@example.com"
    database_url: str = f"sqlite:///{DATA_DIR / 'ipo_watch.sqlite'}"

    anthropic_api_key: str | None = None
    fred_api_key: str | None = None
    kalshi_api_key: str | None = None
    newsapi_key: str | None = None
    finnhub_api_key: str | None = None
    reddit_client_id: str | None = None
    reddit_client_secret: str | None = None

    alert_channel: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


def load_yaml(name: str) -> dict:
    """Load config/<name>.yaml."""
    with open(CONFIG_DIR / f"{name}.yaml") as f:
        return yaml.safe_load(f)
