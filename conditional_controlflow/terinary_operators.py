"""
ternary_operator.py

Topic:
    - Ternary Operator
    - Conditional Expressions
    - Nested Ternary (Use Sparingly)

Real World Application:
    Smart ATM System

Run:
    python ternary_operator.py
"""


def withdrawal_status(balance: float, amount: float) -> str:
    """
    Determines whether a withdrawal is allowed.
    """

    print("\n--- Withdrawal Status ---")

    status = (
        "Withdrawal Approved"
        if balance >= amount
        else "Insufficient Balance"
    )

    print(status)
    return status


def account_type(balance: float) -> str:
    """
    Categorizes the account based on balance.
    """

    print("\n--- Account Type ---")

    account = (
        "Premium Account"
        if balance >= 10000
        else "Standard Account"
    )

    print(account)
    return account


def atm_login(card_inserted: bool) -> None:
    """
    Checks whether the user can access the ATM.
    """

    print("\n--- ATM Login ---")

    message = (
        "Welcome to Smart ATM!"
        if card_inserted
        else "Please Insert Your Card."
    )

    print(message)


def transaction_fee(amount: float) -> None:
    """
    Premium transactions (>= ₹5000) have no fee.
    Others incur a ₹20 fee.
    """

    print("\n--- Transaction Fee ---")

    fee = 0 if amount >= 5000 else 20

    print(f"Transaction Amount : ₹{amount}")
    print(f"Transaction Fee    : ₹{fee}")


def cash_limit(amount: float) -> None:
    """
    Checks if the requested amount is within the daily limit.
    """

    print("\n--- Daily Cash Limit ---")

    result = (
        "Within Daily Limit"
        if amount <= 25000
        else "Daily Limit Exceeded"
    )

    print(result)


def account_category(balance: float) -> None:
    """
    Demonstrates a nested ternary operator.

    Note:
    Nested ternaries should be used sparingly.
    An if-elif-else block is often more readable.
    """

    print("\n--- Account Category ---")

    category = (
        "Premium"
        if balance >= 10000
        else "Standard"
        if balance >= 3000
        else "Basic"
    )

    print(category)


def loan_eligibility(salary: int) -> None:
    """
    Assigns loan eligibility using a ternary operator.
    """

    print("\n--- Loan Eligibility ---")

    result = (
        "Eligible for Loan"
        if salary >= 50000
        else "Not Eligible"
    )

    print(result)


def run() -> None:
    """
    Runs all ternary operator examples.
    """

    print("\n========== TERNARY OPERATOR ==========")

    withdrawal_status(12000, 5000)
    withdrawal_status(2000, 5000)

    account_type(15000)
    account_type(4500)

    atm_login(True)
    atm_login(False)

    transaction_fee(6000)
    transaction_fee(2000)

    cash_limit(10000)
    cash_limit(30000)

    account_category(15000)
    account_category(5000)
    account_category(1000)

    loan_eligibility(70000)
    loan_eligibility(25000)


if __name__ == "__main__":
    run()