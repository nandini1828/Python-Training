from control_flow.ternary import get_status


def test_adult():
    assert get_status(20) == "Adult"


def test_minor():
    assert get_status(15) == "Minor"


def test_boundary():
    assert get_status(18) == "Adult"