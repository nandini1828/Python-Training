"""
conditionals.py

Topic:
    - if
    - if-else
    - if-elif-else
    - Nested if
    - Multiple conditions

Real World Application:
    Smart ATM System

Run:
    python conditionals.py
"""


def verify_card(card_inserted: bool) -> bool:
    """
    Demonstrates a simple if statement.
    """

    print("\n--- Card Verification ---")

    if card_inserted:
        print("Card detected.")
        print("Welcome to Smart ATM.")
        return True
    return False


def pin_verification(entered_pin: int, actual_pin: int) -> bool:
    """
    Demonstrates if-else.
    """

    print("\n--- PIN Verification ---")

    if entered_pin == actual_pin:
        print("PIN Verified.")
        return True
    else:
        print("Invalid PIN.")
        return False


def account_status(balance: float) -> str:
    """
    Demonstrates if-elif-else.
    """

    print("\n--- Account Status ---")

    if balance >= 10000:
        print("Premium Account")
        return "Premium Account"
    elif balance >= 3000:
        print("Standard Account")
        return "Standard Account"
    elif balance > 0:
        print("Low Balance Account")
        return "Low Balance Account"
    else:
        print("Zero Balance Account")
        return "Zero Balance Account"


def withdraw(balance: float, amount: float) -> None:
    """
    Demonstrates nested if statements.
    """

    print("\n--- Cash Withdrawal ---")

    if amount > 0:

        if balance >= amount:
            balance -= amount
            print(f"Withdrawal Successful: ₹{amount}")
            print(f"Remaining Balance: ₹{balance}")

        else:
            print("Insufficient Balance.")

    else:
        print("Invalid Withdrawal Amount.")


def loan_eligibility(
    salary: int,
    credit_score: int,
    existing_loan: bool,
) -> None:
    """
    Demonstrates multiple conditions.
    """

    print("\n--- Loan Eligibility ---")

    if salary >= 50000:

        if credit_score >= 750:

            if not existing_loan:
                print("Congratulations! Loan Approved.")
            else:
                print("Existing loan detected.")
                print("Loan cannot be approved.")

        else:
            print("Poor Credit Score.")

    else:
        print("Salary does not meet eligibility criteria.")


def atm_session() -> None:
    """
    Complete ATM flow using conditionals.
    """

    print("\n==============================")
    print("      SMART ATM SYSTEM")
    print("==============================")

    card_inserted = True

    verify_card(card_inserted)

    if not card_inserted:
        return

    actual_pin = 1234
    entered_pin = 1234

    pin_verification(entered_pin, actual_pin)

    if entered_pin != actual_pin:
        return

    balance = 12000

    account_status(balance)

    withdraw(balance, 2500)

    loan_eligibility(
        salary=65000,
        credit_score=790,
        existing_loan=False,
    )


def run() -> None:
    """
    Runs all demonstrations.
    """

    print("\n========== CONDITIONALS ==========")

    verify_card(True)

    pin_verification(1234, 1234)
    pin_verification(1111, 1234)

    account_status(15000)
    account_status(7000)
    account_status(800)
    account_status(0)

    withdraw(10000, 2000)
    withdraw(1500, 3000)
    withdraw(5000, -200)

    loan_eligibility(70000, 780, False)
    loan_eligibility(45000, 780, False)
    loan_eligibility(70000, 650, False)
    loan_eligibility(70000, 780, True)

    atm_session()


if __name__ == "__main__":
    run()