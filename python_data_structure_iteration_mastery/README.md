# Python Data Structure Iteration & Safety

This project demonstrates Python data structure iteration concepts and safe access patterns in a clean, modular structure.

## Topics Covered

### Data Structure Iteration & Safety
- Lists: indices, slicing, and looping
- List modification trap while iterating
- Dictionaries: `.keys()`, `.values()`, `.items()`
- Dictionary key protection using `.get()` and `defaultdict`
- Sets: fast membership testing and iteration

### Testing
Pytest-based unit tests are included for all major modules.

## Project Structure

```text
python_data_structure_iteration_mastery/
│
├── main.py
├── pytest.ini
├── README.md
│
├── data_structure_iteration/
│   ├── __init__.py
│   ├── list_iteration.py
│   ├── list_modification_trap.py
│   ├── dictionary_iteration.py
│   ├── dictionary_key_protection.py
│   └── set_iteration.py
│
├── tests/
│   ├── test_list_iteration.py
│   ├── test_list_modification_trap.py
│   ├── test_dictionary_iteration.py
│   ├── test_dictionary_key_protection.py
│   └── test_set_iteration.py
│
└── docs/
    └── overview.md