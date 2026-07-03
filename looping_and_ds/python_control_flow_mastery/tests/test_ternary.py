from looping_and_ds.python_control_flow_mastery.conditionals.ternary import get_voting_status, get_parity


def test_voting_status_eligible():
    assert get_voting_status(18) == "Eligible"


def test_voting_status_not_eligible():
    assert get_voting_status(15) == "Not Eligible"


def test_parity_even():
    assert get_parity(8) == "Even"


def test_parity_odd():
    assert get_parity(7) == "Odd"