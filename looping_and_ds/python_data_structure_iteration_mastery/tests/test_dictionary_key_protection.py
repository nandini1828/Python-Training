from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.dictionary_key_protection import (
    safe_get_value,
    count_words_with_defaultdict,
)


def test_safe_get_value_existing_key():
    assert safe_get_value({"name": "Karthik"}, "name") == "Karthik"


def test_safe_get_value_missing_key():
    assert safe_get_value({"name": "Karthik"}, "age", 0) == 0


def test_count_words_with_defaultdict():
    words = ["python", "java", "python", "c", "java", "python"]

    assert count_words_with_defaultdict(words) == {
        "python": 3,
        "java": 2,
        "c": 1,
    }