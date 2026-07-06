"""
Utility functions for loading JSON data in the Iteration Helpers module.
"""

import json
from pathlib import Path


def load_json(file_path):
    file_path = Path(file_path)
    with file_path.open('r', encoding='utf-8') as file:
        return json.load(file)
