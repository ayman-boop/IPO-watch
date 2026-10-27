from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def edgar_fixtures() -> Path:
    """Saved real S-1 / S-1/A / 424B4 documents for offline parser tests."""
    return FIXTURES / "edgar"


@pytest.fixture
def signal_fixtures() -> Path:
    """Saved Kalshi / Polymarket / news / Reddit API responses."""
    return FIXTURES / "signals"
