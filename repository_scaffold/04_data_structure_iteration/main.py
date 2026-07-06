"""
Main entry point for the Data Structure Iteration module.

Run this file to execute demonstrations from all concepts.
"""

from dictionary_iteration.demo import main as dictionary_iteration_demo
from dictionary_key_protection.demo import main as dictionary_key_protection_demo
from list_iteration.demo import main as list_iteration_demo
from list_modification.demo import main as list_modification_demo
from set_iteration.demo import main as set_iteration_demo


def main():
    print("=" * 80)
    print("PYTHON DATA STRUCTURE ITERATION MODULE")
    print("=" * 80)

    list_iteration_demo()
    list_modification_demo()
    dictionary_iteration_demo()
    dictionary_key_protection_demo()
    set_iteration_demo()

    print("\nAll Data Structure Iteration demonstrations completed successfully.")


if __name__ == "__main__":
    main()
