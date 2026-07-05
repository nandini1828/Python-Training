"""
Operations related to loop control statements.
"""


def find_first_failed_transaction(transactions: list[bool]) -> int | None:
    """Return the index of the first failed transaction using break."""
    failed_index = None

    for index, transaction in enumerate(transactions):
        if not transaction:
            failed_index = index
            break

    return failed_index


def filter_active_customers(customers: list[dict]) -> list[dict]:
    """Return only active customers using continue."""
    active_customers = []

    for customer in customers:
        if not customer["active"]:
            continue
        active_customers.append(customer)

    return active_customers


def collect_even_numbers(numbers: list[int]) -> list[int]:
    """Return only even numbers using continue."""
    even_numbers = []

    for number in numbers:
        if number % 2 != 0:
            continue
        even_numbers.append(number)

    return even_numbers


def skip_negative_numbers(numbers: list[int]) -> list[int]:
    """Return numbers excluding negative values using continue."""
    positive_numbers = []

    for number in numbers:
        if number < 0:
            continue
        positive_numbers.append(number)

    return positive_numbers


def first_high_value_sale(sales: list[int], minimum: int) -> int | None:
    """Return the first sale greater than or equal to the minimum using break."""
    result = None

    for sale in sales:
        if sale >= minimum:
            result = sale
            break

    return result


def calculate_running_total(numbers: list[int]) -> int:
    """Calculate the running total."""
    total = 0

    for number in numbers:
        total += number

    return total


def future_discount_feature() -> None:
    """Placeholder for a future discount feature."""
    pass