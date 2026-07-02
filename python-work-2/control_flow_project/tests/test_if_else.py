from control_flow.if_else import grade


def test_grade_a():
    assert grade(95) == "A"


def test_grade_b():
    assert grade(85) == "B"


def test_grade_c():
    assert grade(75) == "C"


def test_grade_d():
    assert grade(60) == "D"


def test_grade_fail():
    assert grade(35) == "Fail"