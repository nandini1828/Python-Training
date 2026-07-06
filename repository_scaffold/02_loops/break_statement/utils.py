"""
utils.py

Reusable utility functions demonstrating break statement usage.
"""


def stop_at(limit: int, stop: int) -> list:
    """
    Returns numbers until stop value is reached.
    """
    result = []

    for i in range(1, limit + 1):
        if i == stop:
            break
        result.append(i)

    return result


def find_first_even(numbers: list) -> int | None:
    """
    Returns first even number or None.
    """
    for num in numbers:
        if num % 2 == 0:
            return num
    return None


def search_item(items: list, target) -> bool:
    """
    Returns True if target found, else False.
    """
    for item in items:
        if item == target:
            return True
    return False


def stop_on_negative(values: list) -> list:
    """
    Returns values until a negative number appears.
    """
    result = []

    for val in values:
        if val < 0:
            break
        result.append(val)

    return result


def first_prime(numbers: list) -> int | None:
    """
    Returns first prime number in list.
    """
    for num in numbers:
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            return num

    return None


def login_success(attempts: int, success_on: int) -> bool:
    """
    Simulates login attempts. Returns True if success occurs.
    """
    current = 1

    while current <= attempts:
        if current == success_on:
            return True
        current += 1

    return False


def process_until_cancel(items: list) -> list:
    """
    Processes items until 'Cancelled' appears.
    """
    result = []

    for item in items:
        if item == "Cancelled":
            break
        result.append(item)

    return result