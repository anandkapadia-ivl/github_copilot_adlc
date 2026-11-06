"""Vercel entrypoint for FastAPI backend."""

import sys
from pathlib import Path

# Ensure backend/src is on the module search path
SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from aimplify_intake.main import app  # noqa: E402
