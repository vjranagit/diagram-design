#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
python3 -m venv "$HERE/.venv"
"$HERE/.venv/bin/python" -m pip install --disable-pip-version-check playwright
PLAYWRIGHT_BROWSERS_PATH="$HERE/.cache/ms-playwright" "$HERE/.venv/bin/python" -m playwright install chromium --only-shell
