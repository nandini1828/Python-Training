"""
config.py
~~~~~~~~~

Configuration for the Repository Scaffold Generator.

Modify only this file when adding/removing modules or concepts.
"""

# =============================================================================
# Repository Name
# =============================================================================

REPOSITORY_NAME = "python_training"

# =============================================================================
# Root Directory
# =============================================================================

OUTPUT_DIRECTORY = "."

# =============================================================================
# Module Configuration
# =============================================================================

MODULES = {
    "01_control_flow": {
        "display_name": "Conditional Control Flow & Decision Making",
        "notes": [
            "01_Introduction",
            "02_If_Elif_Else",
            "03_Truthy_Falsy",
            "04_Logical_Operators",
            "05_Short_Circuit_Evaluation",
            "06_Ternary_Operator",
            "07_Match_Case",
        ],
        "concepts": [
            "if_else",
            "truthy_falsy",
            "logical_operators",
            "short_circuit",
            "ternary_operator",
            "match_case",
        ],
    },
    "02_loops": {
        "display_name": "Loop Foundations & Basic Iteration",
        "notes": [
            "01_Introduction",
            "02_For_Loop",
            "03_While_Loop",
            "04_Break",
            "05_Continue",
            "06_Pass",
            "07_For_Else_While_Else",
        ],
        "concepts": [
            "for_loop",
            "while_loop",
            "break_statement",
            "continue_statement",
            "pass_statement",
            "loop_else",
        ],
    },
    "03_iteration_helpers": {
        "display_name": "Python Iteration Helpers",
        "notes": [
            "01_Introduction",
            "02_Range",
            "03_Enumerate",
            "04_Zip",
            "05_Reversed",
            "06_Sorted",
            "07_Any_All",
        ],
        "concepts": [
            "range_module",
            "enumerate_module",
            "zip_module",
            "reversed_module",
            "sorted_module",
            "any_all",
        ],
    },
    "04_data_structure_iteration": {
        "display_name": "Data Structure Iteration",
        "notes": [
            "01_Introduction",
            "02_List_Iteration",
            "03_List_Modification_Trap",
            "04_Dictionary_Iteration",
            "05_Dictionary_Key_Protection",
            "06_Set_Iteration",
        ],
        "concepts": [
            "list_iteration",
            "list_modification",
            "dictionary_iteration",
            "dictionary_key_protection",
            "set_iteration",
        ],
    },
    "05_comprehensions": {
        "display_name": "Comprehensions",
        "notes": [
            "01_Introduction",
            "02_List_Comprehension",
            "03_Dictionary_Comprehension",
            "04_Set_Comprehension",
            "05_Nested_Comprehension",
        ],
        "concepts": [
            "list_comprehension",
            "dictionary_comprehension",
            "set_comprehension",
            "nested_comprehension",
        ],
    },
    "06_iterators_generators": {
        "display_name": "Iterators & Generators",
        "notes": [
            "01_Introduction",
            "02_Iterator_Protocol",
            "03_Generators",
            "04_Generator_Expressions",
        ],
        "concepts": [
            "iterator_protocol",
            "generators",
            "generator_expressions",
        ],
    },
}

# =============================================================================
# Module Root Files
# =============================================================================

MODULE_ROOT_FILES = [
    "__init__.py",
    "README.md",
    "main.py",
    "logging_config.py",
    "json_query.py",
]

# =============================================================================
# Concept Files
# =============================================================================

CONCEPT_FILES = [
    "__init__.py",
    "README.md",
    "demo.py",
    "utils.py",
]

# =============================================================================
# Test Configuration
# =============================================================================

TEST_FOLDER = "tests"

TEST_PREFIX = "test_"

# =============================================================================
# Notes Configuration
# =============================================================================

NOTES_FOLDER = "Notes"

NOTE_EXTENSION = ".md"

# =============================================================================
# Generation Options
# =============================================================================

CREATE_README = True

CREATE_NOTES = True

CREATE_TESTS = True

CREATE_CONCEPT_README = True

CREATE_CONCEPT_DEMO = True

CREATE_CONCEPT_UTILS = True

CREATE_MAIN = True

CREATE_JSON_QUERY = True

CREATE_LOGGING = True

OVERWRITE_EXISTING = False

# =============================================================================
# Empty File Content
# =============================================================================

EMPTY_PYTHON_FILE = ""

EMPTY_MARKDOWN_FILE = ""

# =============================================================================
# Supported Extensions
# =============================================================================

PYTHON_EXTENSION = ".py"

MARKDOWN_EXTENSION = ".md"