from iteration_helpers.zip_helper import zip_items, zip_longest_items


def test_zip_items():
    assert zip_items(["a", "b"], [1, 2]) == [("a", 1), ("b", 2)]


def test_zip_longest_items():
    assert zip_longest_items(["a", "b", "c"], [1, 2], "Missing") == [
        ("a", 1),
        ("b", 2),
        ("c", "Missing"),
    ]