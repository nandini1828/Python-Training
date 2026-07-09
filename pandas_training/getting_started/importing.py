"""
Demonstrates importing the Pandas library and checking its version.
"""

import pandas as pd


def import_pandas():
    """Print the installed Pandas version."""

    print("=" * 50)
    print("IMPORTING PANDAS")
    print("=" * 50)

    print("Pandas imported successfully.")
    print(f"Pandas Version : {pd.__version__}")


if __name__ == "__main__":
    import_pandas()