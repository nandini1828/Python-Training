from iterators.zip_ops import zip_items


def test_zip_items():
    assert zip_items([1, 2], ["x", "y"]) == [(1, "x"), (2, "y")]
