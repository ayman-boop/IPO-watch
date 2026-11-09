import pytest

import edgar_utils


def test_get_without_user_agent_raises(monkeypatch):
    monkeypatch.delenv("SEC_USER_AGENT", raising=False)
    with pytest.raises(RuntimeError, match="SEC_USER_AGENT"):
        edgar_utils.get("https://data.sec.gov/submissions/CIK0000000000.json")
