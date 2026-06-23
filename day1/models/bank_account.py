"""
Encapsulation Example
"""

class BankAccount:

    def __init__(
        self,
        balance: float
    ) -> None:
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance

    def deposit(
        self,
        amount: float
    ) -> None:
        self.__balance += amount