from looping_and_ds.python_control_flow_mastery.conditionals.truthy_falsy import is_truthy, evaluate_truthy_falsy


def test_empty_list_is_falsy():
    assert is_truthy([]) is False


def test_non_empty_list_is_truthy():
    assert is_truthy([1]) is True


def test_zero_is_falsy():
    assert is_truthy(0) is False


def test_non_zero_is_truthy():
    assert is_truthy(100) is True


def test_evaluate_truthy_falsy_returns_expected_keys():
    result = evaluate_truthy_falsy()

    assert "empty_list" in result
    assert "none_value" in result
    assert result["empty_string"] is False