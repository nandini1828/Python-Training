from utilities.helpers import classify_status


def test_classify_status():
    assert classify_status(0) == "available"
    assert classify_status(1) == "borrowed"
