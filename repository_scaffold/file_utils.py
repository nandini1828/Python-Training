"""
file_utils.py
~~~~~~~~~~~~~

Utility functions for creating directories and files.

Author : Ganesh Bairi
"""

from pathlib import Path
from typing import Iterable


# =============================================================================
# Directory Operations
# =============================================================================

def create_directory(directory: Path) -> None:
    """
    Create a directory if it doesn't exist.
    """

    directory.mkdir(parents=True, exist_ok=True)


# =============================================================================
# File Operations
# =============================================================================

def create_file(
    file_path: Path,
    content: str = "",
    overwrite: bool = False,
) -> None:
    """
    Create a file with optional content.

    Parameters
    ----------
    file_path : Path
        Path of the file.

    content : str
        Content to write.

    overwrite : bool
        Overwrite existing file.
    """

    if file_path.exists() and not overwrite:
        return

    file_path.write_text(
        content,
        encoding="utf-8",
    )


# =============================================================================
# Multiple File Creation
# =============================================================================

def create_files(
    directory: Path,
    files: Iterable[str],
    content: str = "",
    overwrite: bool = False,
) -> None:
    """
    Create multiple files inside a directory.
    """

    for file_name in files:
        create_file(
            directory / file_name,
            content,
            overwrite,
        )


# =============================================================================
# Notes Creation
# =============================================================================

def create_notes(
    notes_directory: Path,
    notes: Iterable[str],
    overwrite: bool = False,
) -> None:
    """
    Create markdown note files.
    """

    create_directory(notes_directory)

    for note in notes:
        create_file(
            notes_directory / f"{note}.md",
            overwrite=overwrite,
        )


# =============================================================================
# Test Creation
# =============================================================================

def create_tests(
    tests_directory: Path,
    concepts: Iterable[str],
    overwrite: bool = False,
) -> None:
    """
    Create pytest files.
    """

    create_directory(tests_directory)

    create_file(
        tests_directory / "__init__.py",
        overwrite=overwrite,
    )

    for concept in concepts:
        create_file(
            tests_directory / f"test_{concept}.py",
            overwrite=overwrite,
        )


# =============================================================================
# Concept Folder Creation
# =============================================================================

def create_concept_folder(
    module_directory: Path,
    concept: str,
    concept_files: Iterable[str],
    overwrite: bool = False,
) -> None:
    """
    Create one concept folder.
    """

    concept_directory = module_directory / concept

    create_directory(concept_directory)

    create_files(
        concept_directory,
        concept_files,
        overwrite=overwrite,
    )


# =============================================================================
# Module Creation
# =============================================================================

def create_module(
    root_directory: Path,
    module_name: str,
    module_config: dict,
    module_files: Iterable[str],
    concept_files: Iterable[str],
    overwrite: bool = False,
) -> None:
    """
    Create complete module structure.
    """

    module_directory = root_directory / module_name

    create_directory(module_directory)

    # ---------------------------------------------------------

    create_files(
        module_directory,
        module_files,
        overwrite=overwrite,
    )

    # ---------------------------------------------------------

    create_notes(
        module_directory / "Notes",
        module_config["notes"],
        overwrite,
    )

    # ---------------------------------------------------------

    create_tests(
        module_directory / "tests",
        module_config["concepts"],
        overwrite,
    )

    # ---------------------------------------------------------

    for concept in module_config["concepts"]:

        create_concept_folder(
            module_directory,
            concept,
            concept_files,
            overwrite,
        )