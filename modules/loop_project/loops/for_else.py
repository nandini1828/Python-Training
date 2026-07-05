"""
Operations related to for-else statements.
"""


def search_employee(employees: list[str], target: str) -> str:
    """Search for an employee."""
    for employee in employees:
        if employee == target:
            return f"{target} found"
    else:
        return f"{target} not found"


def search_policy(policy_numbers: list[int], target: int) -> str:
    """Search for a policy number."""
    for policy in policy_numbers:
        if policy == target:
            return "Policy exists"
    else:
        return "Policy not found"


def find_prime(number: int) -> bool:
    """Return True if the number is prime."""
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    else:
        return True


def locate_product(products: list[str], target: str) -> bool:
    """Return True if the product exists."""
    for product in products:
        if product == target:
            return True
    else:
        return False