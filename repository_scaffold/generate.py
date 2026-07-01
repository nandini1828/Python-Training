"""
generate.py
~~~~~~~~~~~

Repository Scaffold Generator

Run:

    python generate.py

Author : Ganesh Bairi
"""

from pathlib import Path

from config import (
    OUTPUT_DIRECTORY,
    MODULES,
    MODULE_ROOT_FILES,
    CONCEPT_FILES,
    OVERWRITE_EXISTING,
)

from file_utils import create_module


# =============================================================================
# Main Generator
# =============================================================================

def generate_repository() -> None:
    """
    Generate the complete repository structure.
    """

    root_directory = Path(OUTPUT_DIRECTORY)

    root_directory.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Repository Scaffold Generator")
    print("=" * 70)

    print()

    for module_name, module_config in MODULES.items():

        print(f"Creating {module_name}...")

        create_module(
            root_directory=root_directory,
            module_name=module_name,
            module_config=module_config,
            module_files=MODULE_ROOT_FILES,
            concept_files=CONCEPT_FILES,
            overwrite=OVERWRITE_EXISTING,
        )

    print()
    print("=" * 70)
    print("Repository generated successfully.") 
    print("=" * 70)


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    generate_repository()