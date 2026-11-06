"""ASGI entry point."""

import sys
from pathlib import Path

# Ensure src/ directory is on sys.path so aimplify_intake is importable
_src_dir = str(Path(__file__).resolve().parent.parent)
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from aimplify_intake.api.app import create_app

app = create_app()
