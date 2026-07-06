"""
Utility functions for loading JSON data used in examples.
"""

import json
from pathlib import Path


def load_json(file_path):
    """
    Load a JSON file.

    Parameters
    ----------
    file_path : str | Path

    Returns
    -------
    dict | list
    """

    file_path = Path(file_path)

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)