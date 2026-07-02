from conditionals.logical_operators import evaluate_logical_operations, can_access_system


def test_logical_operations():
    result = evaluate_logical_operations(True, False)

    assert result["and_result"] is False
    assert result["or_result"] is True
    assert result["not_first"] is False
    assert result["not_second"] is True


def test_access_system_allowed():
    assert can_access_system(True, True) is True


def test_access_system_denied_for_inactive():
    assert can_access_system(True, False) is False


def test_access_system_denied_for_non_admin():
    assert can_access_system(False, True) is False