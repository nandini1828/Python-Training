from python_control_flow_mastery.comprehensions.list_comprehension import square_numbers
from python_control_flow_mastery.comprehensions.dictionary_comprehension import invert_mapping
from python_control_flow_mastery.comprehensions.set_comprehension import unique_lengths
from python_control_flow_mastery.comprehensions.nested_comprehension import flatten_matrix


def test_square_numbers_returns_squared_values():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]


def test_invert_mapping_swaps_keys_and_values():
    assert invert_mapping({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_unique_lengths_returns_unique_lengths():
    assert unique_lengths(["cat", "dog", "elephant"]) == {3, 3, 8}


def test_flatten_matrix_flattens_values():
    assert flatten_matrix([[1, 2], [3, 4]]) == [1, 2, 3, 4]
