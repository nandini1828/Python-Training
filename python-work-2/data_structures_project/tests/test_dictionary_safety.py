from data_structures.dictionary_safety import (
    safe_get,
    create_default_dictionary,
)


def test_safe_get_existing_key():

    student = {
        "name": "Alice"
    }

    assert safe_get(student, "name") == "Alice"


def test_safe_get_missing_key():

    student = {
        "name": "Alice"
    }

    assert safe_get(student, "age", 0) == 0


def test_default_dictionary():

    marks = create_default_dictionary()

    assert marks["Math"] == 10
    assert marks["Science"] == 20