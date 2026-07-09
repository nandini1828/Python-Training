"""
logical_operators.py

Topic:
    - and
    - or
    - not
    - Combining multiple conditions

Real World Application:
    Smart ATM System

Run:
    python logical_operators.py
"""


def login(card_inserted: bool, pin_verified: bool) -> bool:
    """
    User can log in only if both the card is inserted
    and the PIN is correct.
    """

    print("\n--- Login Authentication (AND) ---")

    if card_inserted and pin_verified:
        print("Login Successful.")
        return True
    else:
        print("Login Failed.")
        return False


def cash_withdrawal(balance: float, amount: float) -> bool:
    """
    Withdrawal is allowed only when:
    1. Amount is positive.
    2. Sufficient balance exists.
    """

    print("\n--- Cash Withdrawal (AND) ---")

    if amount > 0 and balance >= amount:
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance - amount}")
        return True
    else:
        print("Withdrawal Failed.")
        return False


def premium_lounge(premium_customer: bool, staff_member: bool) -> bool:
    """
    A premium customer OR a bank staff member
    can access the premium lounge.
    """

    print("\n--- Premium Lounge Access (OR) ---")

    if premium_customer or staff_member:
        print("Access Granted.")
        return True
    else:
        print("Access Denied.")
        return False


def online_banking(account_locked: bool) -> None:
    """
    Access is allowed only if the account
    is NOT locked.
    """

    print("\n--- Online Banking (NOT) ---")

    if not account_locked:
        print("Login Allowed.")
    else:
        print("Account Locked.")


def atm_service(
    card_inserted: bool,
    pin_verified: bool,
    account_locked: bool,
) -> None:
    """
    Demonstrates combining AND and NOT.
    """

    print("\n--- ATM Service ---")

    if card_inserted and pin_verified and not account_locked:
        print("ATM Services Available.")
    else:
        print("Unable to Continue.")


def loan_approval(
    salary: int,
    credit_score: int,
    existing_loan: bool,
) -> None:
    """
    Demonstrates multiple logical operators together.
    """

    print("\n--- Loan Approval ---")

    if (
        salary >= 50000
        and credit_score >= 750
        and not existing_loan
    ):
        print("Loan Approved.")
    else:
        print("Loan Rejected.")


def security_alert(
    wrong_pin_attempts: int,
    suspicious_activity: bool,
) -> None:
    """
    Demonstrates OR operator.
    """

    print("\n--- Security Alert ---")

    if wrong_pin_attempts >= 3 or suspicious_activity:
        print("Account Temporarily Blocked.")
    else:
        print("Account Safe.")


def run() -> None:
    """
    Runs all Logical Operator examples.
    """

    print("\n========== LOGICAL OPERATORS ==========")

    login(True, True)
    login(True, False)

    cash_withdrawal(10000, 2500)
    cash_withdrawal(1500, 3000)

    premium_lounge(True, False)
    premium_lounge(False, True)
    premium_lounge(False, False)

    online_banking(False)
    online_banking(True)

    atm_service(True, True, False)
    atm_service(True, True, True)

    loan_approval(70000, 790, False)
    loan_approval(70000, 650, False)
    loan_approval(70000, 790, True)

    security_alert(1, False)
    security_alert(3, False)
    security_alert(0, True)


if __name__ == "__main__":
    run()