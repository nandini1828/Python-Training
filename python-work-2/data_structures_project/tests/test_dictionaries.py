from data_structures.dictionaries import (
    get_keys,
    get_values,
    get_items,
)


def test_get_keys():
    student = {
        "name": "Alice",
        "age": 22,
        "marks": 90,
    }

    assert list(get_keys(student)) == [
        "name",
        "age",
        "marks",
    ]


def test_get_values():
    student = {
        "name": "Alice",
        "age": 22,
        "marks": 90,
    }

    assert list(get_values(student)) == [
        "Alice",
        22,
        90,
    ]


def test_get_items():
    student = {
        "name": "Alice",
        "age": 22,
        "marks": 90,
    }

    expected = [
        ("name", "Alice"),
        ("age", 22),
        ("marks", 90),
    ]

    assert list(get_items(student)) == expected