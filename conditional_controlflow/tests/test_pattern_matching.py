from control_flow.pattern_matching import (
    atm_menu,
    transaction_status,
)


def test_atm_menu():
    assert atm_menu(1) == "Cash Withdrawal Selected."
    assert atm_menu(2) == "Cash Deposit Selected."
    assert atm_menu(10) == "Invalid Menu Option."


def test_transaction_status():
    assert transaction_status("success") == "Transaction Completed Successfully."
    assert transaction_status("failed") == "Transaction Failed."
    assert transaction_status("pending") == "Transaction is Still Processing."
    assert transaction_status("xyz") == "Unknown Transaction Status."