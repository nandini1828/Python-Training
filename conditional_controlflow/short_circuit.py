"""
short_circuit.py

Topic:
    - Short-Circuit Evaluation
    - and
    - or

Real World Application:
    Smart ATM System

Run:
    python short_circuit.py
"""


def verify_card(card_inserted: bool) -> bool:
    """
    Simulates checking whether a card is inserted.
    """

    print("Checking card...")

    return card_inserted


def verify_pin(pin: int) -> bool:
    """
    Simulates PIN verification.
    """

    print("Verifying PIN...")

    return pin == 1234


def check_balance(balance: float, amount: float) -> bool:
    """
    Simulates checking account balance.
    """

    print("Checking account balance...")

    return balance >= amount


def process_withdrawal(balance: float, amount: float) -> None:
    """
    Withdrawal should happen only when:
    1. Card is inserted
    2. PIN is correct
    3. Balance is sufficient

    Demonstrates short-circuit with AND.
    """

    print("\n--- Withdrawal Request ---")

    if (
        verify_card(True)
        and verify_pin(1234)
        and check_balance(balance, amount)
    ):
        print(f"Withdrawal of ₹{amount} Successful.")
    else:
        print("Withdrawal Failed.")


def failed_card_demo() -> None:
    """
    Since the first condition is False,
    Python skips the remaining conditions.
    """

    print("\n--- Failed Card Demo ---")

    if (
        verify_card(False)
        and verify_pin(1234)
        and check_balance(10000, 2000)
    ):
        print("Transaction Successful.")
    else:
        print("Transaction Cancelled.")


def failed_pin_demo() -> None:
    """
    Card passes.
    PIN fails.
    Balance check is skipped.
    """

    print("\n--- Failed PIN Demo ---")

    if (
        verify_card(True)
        and verify_pin(1111)
        and check_balance(10000, 2000)
    ):
        print("Transaction Successful.")
    else:
        print("Transaction Cancelled.")


def customer_support(premium_customer: bool) -> bool:
    """
    Simulates checking premium customer status.
    """

    print("Checking Premium Membership...")

    return premium_customer


def bank_manager_available(manager_available: bool) -> bool:
    """
    Simulates checking manager availability.
    """

    print("Checking Manager Availability...")

    return manager_available


def support_demo() -> None:
    """
    Demonstrates short-circuit using OR.

    If the customer is premium,
    Python won't check the manager.
    """

    print("\n--- Customer Support (OR) ---")

    if (
        customer_support(True)
        or bank_manager_available(True)
    ):
        print("Support Available.")
    else:
        print("No Support Available.")


def support_demo_two() -> None:
    """
    First condition is False,
    so Python evaluates the second condition.
    """

    print("\n--- Customer Support (OR) ---")

    if (
        customer_support(False)
        or bank_manager_available(True)
    ):
        print("Support Available.")
    else:
        print("No Support Available.")


def run() -> None:
    """
    Runs all short-circuit demonstrations.
    """

    print("\n========== SHORT-CIRCUIT EVALUATION ==========")

    process_withdrawal(10000, 2500)

    failed_card_demo()

    failed_pin_demo()

    support_demo()

    support_demo_two()


if __name__ == "__main__":
    run()