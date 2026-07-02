from conditionals.match_case import get_day_category, traffic_signal_action


def test_day_category_weekend():
    assert get_day_category("Sunday") == "Weekend"


def test_day_category_monday():
    assert get_day_category("Monday") == "Start of Week"


def test_day_category_regular():
    assert get_day_category("Wednesday") == "Regular Day"


def test_traffic_signal_red():
    assert traffic_signal_action("red") == "Stop"


def test_traffic_signal_invalid():
    assert traffic_signal_action("blue") == "Invalid Signal"