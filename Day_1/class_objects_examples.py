"""Example programs for Classes and Objects section.
"""

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def show_balance(self):
        print(f"Balance: {self.balance}")


def demo():
    print("Student demo:")
    student = Student("Vamshi", 101)
    student.display()
    print()
    print("BankAccount demo:")
    account = BankAccount(1000)
    account.deposit(500)
    account.show_balance()


if __name__ == "__main__":
    demo()
