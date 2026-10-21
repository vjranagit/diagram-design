#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
test -x "$HERE/.venv/bin/python" || { echo '{"ok":false,"error":"run scripts/setup.sh first"}'; exit 1; }
python3 "$HERE/scripts/build.py" "$1" "$2"
