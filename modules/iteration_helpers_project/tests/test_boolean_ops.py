from iterators.boolean_ops import has_all_true, has_any_true


def test_boolean_helpers():
    assert has_any_true([False, True, False]) is True
    assert has_any_true([False, False]) is False
    assert has_all_true([True, True, True]) is True
    assert has_all_true([True, False, True]) is False
