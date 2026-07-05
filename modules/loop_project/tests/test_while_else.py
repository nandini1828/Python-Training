from modules.loop_project.loops.while_else import *


def test_verify_pin_success():
    assert verify_pin("1234", ["1111", "1234"])


def test_verify_pin_failure():
    assert not verify_pin("1234", ["1111", "2222"])


def test_search_number():
    assert search_number([5, 10, 15], 10)


def test_search_number_false():
    assert not search_number([1, 2], 10)


def test_countdown():
    assert countdown(5) == 0


def test_password_attempts():
    assert password_attempts("admin", ["root", "admin"])


def test_password_attempts_failure():
    assert not password_attempts("admin", ["user", "guest"])