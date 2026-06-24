"""Pytest configuration helpers.

Ensure the project root is on sys.path so tests can import the package
when running pytest from the workspace root.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Add the workspace root (two parents up from this tests folder) to sys.path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
