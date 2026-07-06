"""
test_data_structure_iteration.py

Unit tests for data_structure_iteration module.

Run:
    pytest test_data_structure_iteration.py -v
"""

"""
test_data_structure_iteration.py

Legacy module-level smoke tests for the data_structure_iteration package.
"""

import data_structure_iteration


def test_data_structure_iteration_package_import():
    assert hasattr(data_structure_iteration, "list_iteration_and_slicing")
    assert hasattr(data_structure_iteration, "list_modification_trap")
    assert hasattr(data_structure_iteration, "dictionary_iteration")
    assert hasattr(data_structure_iteration, "dictionary_key_protection")
    assert hasattr(data_structure_iteration, "set_membership_and_looping")


def test_data_structure_iteration_run():
    assert callable(data_structure_iteration.run)
