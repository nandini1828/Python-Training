from conditionals.if_else import classify_number, check_pass_status


def test_classify_positive():
    assert classify_number(5) == "Positive"


def test_classify_negative():
    assert classify_number(-10) == "Negative"


def test_classify_zero():
    assert classify_number(0) == "Zero"


def test_check_pass_status_pass():
    assert check_pass_status(50) == "Pass"


def test_check_pass_status_fail():
    assert check_pass_status(20) == "Fail"