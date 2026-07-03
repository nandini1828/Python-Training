from looping_and_ds.python_iteration_helpers_mastery.iteration_helpers.any_all_helper import check_any, check_all


def test_check_any():
    assert check_any([False, False, True]) is True


def test_check_any_all_false():
    assert check_any([False, False, False]) is False


def test_check_all():
    assert check_all([True, True, True]) is True


def test_check_all_with_false():
    assert check_all([True, False, True]) is False