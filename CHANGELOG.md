# Changelog

## Unreleased — prepare for open source

- Added an MIT `LICENSE`.
- Rewrote `README.md` for outside readers: status, step table, setup, disclaimer.
- Moved the step 1 notes from `Instructions.txt` to `docs/steps/01_list_ipos.txt`.
- Renamed `changes.txt` to this `CHANGELOG.md`.
- Stopped tracking `.claude/` (local editor tooling).
- Added a GitHub Actions workflow that runs the tests on each push and pull request.
- Added `tests/test_edgar_utils.py` (offline tests, no SEC requests).

## 2026-11-03 — Pinned dependencies, location-independent `.env` loading

- `requirements.txt`: each direct dependency is pinned to the tested version.
  `requirements.lock` holds the full `pip freeze` output
  (rebuild with `.venv/bin/pip freeze > requirements.lock`).
- `scripts/edgar_utils.py`:
  - `.env` is found from the project root, so scripts run from any folder.
  - A missing `.env` no longer crashes the import.
  - Variables already set in the shell win over `.env`.
  - `get()` raises a clear `RuntimeError` if `SEC_USER_AGENT` is not set.
- Not added yet on purpose: LightGBM and the later-phase packages from
  `docs/PLAN.txt` (pydantic, sqlalchemy, fastapi, shap, xgboost, an LLM SDK).

## 2026-10-27 — Restart on a smaller design

- Replaced the full-scale package skeleton (database, collectors, signals) with a
  small step-by-step pipeline. See `docs/START_SMALL.txt`. The old layout is in
  commit `53e802a`.
