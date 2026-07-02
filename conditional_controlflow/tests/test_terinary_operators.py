from control_flow.ternary_operator import (
    withdrawal_status,
    account_type,
)


def test_withdrawal_status():
    assert withdrawal_status(10000, 5000) == "Withdrawal Approved"
    assert withdrawal_status(1000, 5000) == "Insufficient Balance"


def test_account_type():
    assert account_type(15000) == "Premium Account"
    assert account_type(4000) == "Standard Account"