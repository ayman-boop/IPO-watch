#!/usr/bin/env bash
# PostToolUse hook: run the project's tests after Claude edits a file.
# Auto-detects the test runner. Exits 2 on failure so the output is fed back to Claude.
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

if [ -f package.json ] && grep -q '"test"' package.json; then
  cmd="npm test --silent"
elif [ -f pyproject.toml ] || [ -f pytest.ini ] || [ -f setup.cfg ] || [ -d tests ] || ls test_*.py >/dev/null 2>&1; then
  if [ -x .venv/bin/python ]; then cmd=".venv/bin/python -m pytest -q"; else cmd="python3 -m pytest -q"; fi
elif [ -f go.mod ]; then
  cmd="go test ./..."
elif [ -f Cargo.toml ]; then
  cmd="cargo test --quiet"
else
  exit 0  # no tests set up yet
fi

out=$($cmd 2>&1)
status=$?
# pytest exit 5 = no tests collected; don't treat as failure
if [ $status -ne 0 ] && ! { [[ $cmd == *pytest* ]] && [ $status -eq 5 ]; }; then
  echo "Tests failed after edit ($cmd):" >&2
  echo "$out" | tail -60 >&2
  exit 2
fi
exit 0
