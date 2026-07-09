"""
Main Program
"""

import importlib


modules = [
    "modules.01_getting_started",
    "modules.02_data_inspection",
    "modules.03_selection_filtering",
    "modules.04_data_cleaning",
    "modules.05_grouping_sorting_combining",
]


def main():

    for module_name in modules:

        module = importlib.import_module(module_name)

        module.run()


if __name__ == "__main__":
    main()