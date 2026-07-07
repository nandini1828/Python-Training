from control_flow.match_case import day


def test_monday():
    assert day(1) == "Monday"


def test_tuesday():
    assert day(2) == "Tuesday"


def test_wednesday():
    assert day(3) == "Wednesday"


def test_invalid_day():
    assert day(10) == "Invalid"