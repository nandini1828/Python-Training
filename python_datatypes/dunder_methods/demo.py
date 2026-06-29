"""
Demo Program for Dunder Methods
"""

from dunder_methods.dunder_examples import (
    BankAccount
)


def main():
    """
    Driver Function
    """

    account = BankAccount(
        "Sagar",
        150000
    )

    print("\nUsing __str__()")
    print(account)

    print("\nUsing __repr__()")
    print(repr(account))

    print("\nUsing __len__()")
    print(len(account))


if __name__ == "__main__":
    main()