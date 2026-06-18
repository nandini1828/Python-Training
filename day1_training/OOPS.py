#Classes and Objects
"""
Product Catalog System

Represent products using classes.
"""


class Product:
    """Represents a product."""


laptop = Product()
mouse = Product()

print(type(laptop))

#Constructor (__init__)
"""
Employee Registration System
"""


class Employee:
    """
    Create employee objects with details.
    """

    def __init__(
        self,
        employee_id,
        name
    ):
        self.employee_id = employee_id
        self.name = name


employee = Employee(
    101,
    "John"
)

print(employee.name)

#Instance Variables
"""
Each employee has unique information.
"""


class Employee:

    def __init__(
        self,
        employee_id
    ):
        self.employee_id = employee_id


employee1 = Employee(101)
employee2 = Employee(102)

print(employee1.employee_id)
print(employee2.employee_id)

#Class Variables

"""
Company details shared by all employees.
"""


class Employee:

    company_name = (
        "ABC Technologies"
    )


employee1 = Employee()
employee2 = Employee()

print(employee1.company_name)
print(employee2.company_name)

#Instance Methods
"""
Display employee salary details.
"""


class Employee:

    def __init__(
        self,
        salary
    ):
        self.salary = salary

    def display_salary(self):
        """
        Display employee salary.
        """
        print(
            f"Salary: {self.salary}"
        )


employee = Employee(80000)

employee.display_salary()

#Static Methods
"""
Utility functions independent of objects.
"""


class TaxCalculator:

    @staticmethod
    def calculate_tax(
        amount
    ):
        """
        Calculate tax amount.
        """
        return amount * 0.10


print(
    TaxCalculator.calculate_tax(
        50000
    )
)

#Class Methods

"""
Track total employees created.
"""


class Employee:

    total_employees = 0

    def __init__(self):
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(
        cls
    ):
        """
        Return total employees.
        """
        return cls.total_employees


Employee()
Employee()
Employee()

print(
    Employee.get_total_employees()
)

#Encapsulation

"""
Protect account balance from direct access.
"""


class BankAccount:

    def __init__(
        self,
        balance
    ):
        self.__balance = balance

    def get_balance(self):
        """
        Read balance safely.
        """
        return self.__balance


account = BankAccount(
    10000
)

print(
    account.get_balance()
)

#Inheritance
"""
Developer inherits common employee features.
"""


class Employee:

    def login(self):
        print(
            "Employee Logged In"
        )


class Developer(Employee):

    def write_code(self):
        print(
            "Writing Python Code"
        )


developer = Developer()

developer.login()
developer.write_code()

#Multilevel Inheritance

"""
Organization Structure.
"""


class Employee:

    def login(self):
        print("Login")


class Manager(Employee):

    def approve_leave(self):
        print(
            "Leave Approved"
        )


class Director(Manager):

    def approve_budget(self):
        print(
            "Budget Approved"
        )


director = Director()

director.login()
director.approve_leave()
director.approve_budget()

#Polymorphism
"""
Send notifications through different channels.
"""


class EmailNotification:

    def send(self):
        print(
            "Email Sent"
        )


class SMSNotification:

    def send(self):
        print(
            "SMS Sent"
        )


def notify(
    notification
):
    """
    Accept any notification object.
    """
    notification.send()


notify(
    EmailNotification()
)

notify(
    SMSNotification()
)

#Abstraction
"""
Hide payment implementation details.
"""

from abc import (
    ABC,
    abstractmethod
)


class Payment(
    ABC
):

    @abstractmethod
    def pay(self):
        """
        Force subclasses
        to implement payment.
        """


class CreditCardPayment(
    Payment
):

    def pay(self):
        print(
            "Credit Card Payment Successful"
        )


payment = (
    CreditCardPayment()
)

payment.pay()

