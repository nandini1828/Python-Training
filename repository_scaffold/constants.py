"""
constants.py
~~~~~~~~~~~~

This module contains all reusable constants used by the
Repository Scaffold Generator.

Author : Ganesh Bairi
"""

# =============================================================================
# General
# =============================================================================

DEFAULT_ENCODING = "utf-8"

# =============================================================================
# Folder Names
# =============================================================================

NOTES_FOLDER = "Notes"
TESTS_FOLDER = "tests"

# =============================================================================
# Common File Names
# =============================================================================

README_FILE = "README.md"
INIT_FILE = "__init__.py"

MAIN_FILE = "main.py"
LOGGING_CONFIG_FILE = "logging_config.py"
JSON_QUERY_FILE = "json_query.py"

DEMO_FILE = "demo.py"
UTILS_FILE = "utils.py"

# =============================================================================
# File Extensions
# =============================================================================

MARKDOWN_EXTENSION = ".md"
PYTHON_EXTENSION = ".py"

# =============================================================================
# Concept Folder Files
# =============================================================================

CONCEPT_FILES = [
    README_FILE,
    INIT_FILE,
    DEMO_FILE,
    UTILS_FILE,
]

# =============================================================================
# Module Root Files
# =============================================================================

MODULE_FILES = [
    README_FILE,
    INIT_FILE,
    MAIN_FILE,
    LOGGING_CONFIG_FILE,
    JSON_QUERY_FILE,
]

# =============================================================================
# Root Folders
# =============================================================================

ROOT_FOLDERS = [
    NOTES_FOLDER,
    TESTS_FOLDER,
]

# =============================================================================
# Supported File Types
# =============================================================================

TEXT_FILE_TYPES = (
    MARKDOWN_EXTENSION,
    PYTHON_EXTENSION,
)