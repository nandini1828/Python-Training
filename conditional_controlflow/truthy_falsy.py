"""
truthy_falsy.py

Topic:
    - Truthy Values
    - Falsy Values
    - bool() conversion
    - Using truthy/falsy in real-world applications

Real World Application:
    Smart ATM System

Run:
    python truthy_falsy.py
"""


class ShoppingBasket:
    """A custom object whose truthiness comes from __bool__()."""

    def __init__(self, items: list[str]) -> None:
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return len(self.items) > 2


def custom_truthiness_demo() -> None:
    """Demonstrates how a class can define its own truthiness."""
    print("\n--- Custom Truthiness ---")

    empty_basket = ShoppingBasket([])
    small_basket = ShoppingBasket(["book"])
    full_basket = ShoppingBasket(["book", "pen", "pencil"])

    for basket in (empty_basket, small_basket, full_basket):
        print(f"  Items: {basket.items} -> bool(basket) = {bool(basket)}")

    print("  Note: __bool__() takes precedence over __len__() when both exist.")


def card_status(card: str | None) -> bool:
    """
    Demonstrates how None behaves as False.
    """

    print("\n--- Card Status ---")

    if card:
        print(f"Card '{card}' inserted.")
        return True
    else:
        print("No card detected.")
        return False


def pin_validation(pin: str) -> bool:
    """
    Empty string is falsy.
    """

    print("\n--- PIN Validation ---")

    if pin:
        print("PIN entered.")
        return True
    else:
        print("PIN cannot be empty.")
        return False


def transaction_history(history: list) -> None:
    """
    Empty list is falsy.
    """

    print("\n--- Transaction History ---")

    if history:
        print("Recent Transactions:")

        for transaction in history:
            print("-", transaction)
    else:
        print("No transaction history available.")


def offers_available(offers: dict) -> None:
    """
    Empty dictionary is falsy.
    """

    print("\n--- Bank Offers ---")

    if offers:
        print("Available Offers:")

        for offer, discount in offers.items():
            print(f"{offer}: {discount}")
    else:
        print("No offers available.")


def active_services(services: set) -> None:
    """
    Empty set is falsy.
    """

    print("\n--- Active Services ---")

    if services:
        print("Enabled Services:")

        for service in services:
            print("-", service)
    else:
        print("No banking services activated.")


def minimum_balance(balance: float) -> None:
    """
    Zero is falsy.
    """

    print("\n--- Balance Check ---")

    if balance:
        print(f"Available Balance: ₹{balance}")
    else:
        print("Your account balance is ₹0.")


def bool_conversion_demo() -> None:
    """
    Demonstrates bool() conversion.
    """

    print("\n--- bool() Conversion ---")

    values = [
        [],
        {},
        set(),
        "",
        None,
        0,
        100,
        "ATM",
        [1],
        {"user": "Rahul"},
        {1, 2},
        -25,
    ]

    for value in values:
        print(f"{repr(value):20} -> {bool(value)}")


def atm_login(card, pin) -> None:
    """
    Practical truthy/falsy example.
    """

    print("\n--- ATM Login ---")

    if card and pin:
        print("Proceeding to authentication...")
    else:
        print("Card or PIN missing.")


def run() -> None:
    """
    Runs all Truthy/Falsy examples.
    """

    print("\n========== TRUTHY & FALSY ==========")

    card_status("HDFC Debit Card")
    card_status(None)

    pin_validation("1234")
    pin_validation("")

    transaction_history([
        "Withdraw ₹2000",
        "Deposit ₹5000",
        "Balance Enquiry"
    ])

    transaction_history([])

    offers_available({
        "Movie Tickets": "20% OFF",
        "Fuel Cashback": "5%"
    })

    offers_available({})

    active_services({
        "UPI",
        "Net Banking",
        "SMS Alerts"
    })

    active_services(set())

    minimum_balance(12000)
    minimum_balance(0)

    bool_conversion_demo()
    custom_truthiness_demo()

    atm_login("Debit Card", "1234")
    atm_login(None, "1234")
    atm_login("Debit Card", "")
    atm_login(None, "")


if __name__ == "__main__":
    run()