"""
==================================================
Module: Dunder Methods
Topic: Magic Methods
Author: Sagar

Description:
Demonstrates common dunder methods using
a BankAccount example.
==================================================
"""


class BankAccount:
    """
    Bank Account Class
    """

    def __init__(
        self,
        account_holder,
        balance
    ):
        """
        Constructor
        """

        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        """
        User Friendly Representation
        """

        return (
            f"Account Holder: {self.account_holder}, "
            f"Balance: ₹{self.balance}"
        )

    def __repr__(self):
        """
        Developer Representation
        """

        return (
            f"BankAccount("
            f"'{self.account_holder}', "
            f"{self.balance})"
        )

    def __len__(self):
        """
        Length of account holder name.
        """

        return len(self.account_holder)

    def __eq__(self, other: object) -> bool:
        """Equality based on balance and account holder."""

        if not isinstance(other, BankAccount):
            return NotImplemented
        return (self.account_holder, self.balance) == (other.account_holder, other.balance)

    def __lt__(self, other: object) -> bool:
        """Less-than based on balance."""

        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __add__(self, other: object):
        """Combine two accounts into a new aggregated account (summing balances)."""

        if not isinstance(other, BankAccount):
            return NotImplemented
        combined_holder = f"{self.account_holder}&{other.account_holder}"
        return BankAccount(combined_holder, self.balance + other.balance)
