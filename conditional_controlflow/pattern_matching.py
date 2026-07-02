"""
pattern_matching.py

Topic:
    - match-case
    - Multiple Cases
    - OR Pattern (|)
    - Guard (if)
    - Default Case (_)

Real World Application:
    Smart ATM System

Run:
    python pattern_matching.py
"""


def atm_menu(option: int) -> None:
    """
    Demonstrates a basic match-case statement.
    """

    print("\n--- ATM Menu ---")

    match option:
        case 1:
            print("Cash Withdrawal Selected.")

        case 2:
            print("Cash Deposit Selected.")

        case 3:
            print("Balance Enquiry Selected.")

        case 4:
            print("Mini Statement Selected.")

        case 5:
            print("PIN Change Selected.")

        case 6:
            print("Thank you for using Smart ATM.")

        case _:
            print("Invalid Menu Option.")


def transaction_status(status: str) -> None:
    """
    Demonstrates matching string values.
    """

    print("\n--- Transaction Status ---")

    match status.lower():
        case "success":
            print("Transaction Completed Successfully.")

        case "failed":
            print("Transaction Failed.")

        case "pending":
            print("Transaction is Still Processing.")

        case _:
            print("Unknown Transaction Status.")


def customer_support(option: str) -> None:
    """
    Demonstrates OR Pattern using |.
    """

    print("\n--- Customer Support ---")

    match option.lower():
        case "call" | "phone":
            print("Connecting to Customer Care...")

        case "email" | "mail":
            print("Opening Email Support...")

        case "chat":
            print("Starting Live Chat...")

        case _:
            print("Support Option Not Available.")


def withdrawal_limit(amount: float) -> None:
    """
    Demonstrates Guard Conditions.
    """

    print("\n--- Withdrawal Request ---")

    match amount:

        case amount if amount <= 0:
            print("Invalid Withdrawal Amount.")

        case amount if amount <= 10000:
            print(f"Withdrawal of ₹{amount} Approved.")

        case amount if amount <= 25000:
            print(f"Withdrawal of ₹{amount} Requires OTP Verification.")

        case _:
            print("Daily Withdrawal Limit Exceeded.")


def account_type(balance: float) -> None:
    """
    Demonstrates guards with ranges.
    """

    print("\n--- Account Classification ---")

    match balance:

        case balance if balance >= 10000:
            print("Premium Account")

        case balance if balance >= 3000:
            print("Standard Account")

        case balance if balance > 0:
            print("Basic Account")

        case _:
            print("Zero Balance Account")


def run() -> None:
    """
    Runs all pattern matching examples.
    """

    print("\n========== PATTERN MATCHING ==========")

    atm_menu(1)
    atm_menu(3)
    atm_menu(5)
    atm_menu(10)

    transaction_status("success")
    transaction_status("failed")
    transaction_status("pending")
    transaction_status("unknown")

    customer_support("call")
    customer_support("email")
    customer_support("chat")
    customer_support("sms")

    withdrawal_limit(5000)
    withdrawal_limit(15000)
    withdrawal_limit(30000)
    withdrawal_limit(-500)

    account_type(15000)
    account_type(6000)
    account_type(800)
    account_type(0)


if __name__ == "__main__":
    run()