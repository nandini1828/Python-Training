from loops.while_loop import countdown


def test_countdown():

    assert countdown(5) == [5, 4, 3, 2, 1]


def test_countdown_zero():

    assert countdown(0) == []