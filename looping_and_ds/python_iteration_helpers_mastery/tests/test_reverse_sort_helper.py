from looping_and_ds.python_iteration_helpers_mastery.iteration_helpers.reverse_sort_helper import (
    reverse_items,
    sort_numbers,
    sort_records_by_key,
)


def test_reverse_items():
    assert reverse_items([1, 2, 3]) == [3, 2, 1]


def test_sort_numbers():
    assert sort_numbers([5, 2, 4, 1]) == [1, 2, 4, 5]


def test_sort_records_by_key():
    records = [
        {"name": "Karthik", "age": 21},
        {"name": "Rahul", "age": 19},
        {"name": "Anil", "age": 23},
    ]

    assert sort_records_by_key(records, "age") == [
        {"name": "Rahul", "age": 19},
        {"name": "Karthik", "age": 21},
        {"name": "Anil", "age": 23},
    ]