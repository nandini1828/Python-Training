"""
utils.py

Reusable helper functions demonstrating logical operators.
"""


def can_vote(age: int, citizen: bool) -> bool:
    return age >= 18 and citizen


def validate_login(username, password, valid_user, valid_password):
    return username == valid_user and password == valid_password


def has_access(is_admin: bool, is_manager: bool) -> bool:
    return is_admin or is_manager


def can_drive(age: int, has_license: bool) -> bool:
    return age >= 18 and has_license


def is_scholarship_eligible(marks: int, income: int) -> bool:
    return marks >= 90 and income < 300000


def can_withdraw(balance: float, amount: float) -> bool:
    return amount > 0 and amount <= balance


def should_apply_discount(member: bool, amount: float) -> bool:
    return member or amount >= 5000


def employee_entry(employee: bool, has_id: bool) -> bool:
    return employee and has_id


def should_carry_umbrella(raining: bool, umbrella: bool) -> bool:
    return raining and not umbrella


def needs_login(logged_in: bool) -> bool:
    return not logged_in