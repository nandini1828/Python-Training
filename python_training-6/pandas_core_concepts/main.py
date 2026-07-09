"""
main.py

Entry point for the Pandas Core Concepts module.
Runs all topic demonstrations.
"""

import importlib


getting_started = importlib.import_module("modules.01_getting_started")
inspecting_data = importlib.import_module("modules.02_inspecting_data")
selecting_filtering = importlib.import_module("modules.03_selecting_filtering")
cleaning_editing = importlib.import_module("modules.04_cleaning_editing")
grouping_sorting_combining = importlib.import_module(
    "modules.05_grouping_sorting_combining"
)


def main():
    print("=" * 60)
    print("           PANDAS CORE CONCEPTS")
    print("=" * 60)

    print("\nRunning Module 1: Getting Started")
    getting_started.run()

    print("\nRunning Module 2: Inspecting Data")
    inspecting_data.run()

    print("\nRunning Module 3: Selecting & Filtering")
    selecting_filtering.run()

    print("\nRunning Module 4: Cleaning & Editing")
    cleaning_editing.run()

    print("\nRunning Module 5: Grouping, Sorting & Combining")
    grouping_sorting_combining.run()

    print("\n" + "=" * 60)
    print("All modules executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()