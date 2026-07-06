"""
Examples demonstrating Python's for-else and while-else constructs.

The else block executes only when the loop completes normally
without encountering a break statement.

Topics covered:
- for-else
- while-else
- Searching
- Prime numbers
- Login attempts
- Retry logic

Author: Python Training
"""

from __future__ import annotations


def search_item(items: list[str], target: str) -> bool:
    """
    Search for an item using for-else.

    Args:
        items:
            Collection to search.

        target:
            Item to search for.

    Returns:
        True if found, otherwise False.
    """
    for item in items:
        if item == target:
            break
    else:
        return False

    return True


def find_employee(
    employees: list[str],
    employee: str,
) -> str:
    """
    Search for an employee.

    Args:
        employees:
            Employee names.

        employee:
            Employee to search.

    Returns:
        Search result.
    """
    for name in employees:
        if name == employee:
            return f"{employee} found."
    else:
        return f"{employee} not found."


def is_prime(number: int) -> bool:
    """
    Determine whether a number is prime.

    Args:
        number:
            Integer to check.

    Returns:
        True if prime.
    """
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            break
    else:
        return True

    return False


def login_attempts(
    passwords: list[str],
    correct_password: str,
) -> bool:
    """
    Simulate login attempts.

    Args:
        passwords:
            Attempted passwords.

        correct_password:
            Expected password.

    Returns:
        True if login succeeds.
    """
    for password in passwords:
        if password == correct_password:
            return True
    else:
        return False


def retry_connection(
    success_on_attempt: int,
    maximum_attempts: int,
) -> bool:
    """
    Simulate retry logic using while-else.

    Args:
        success_on_attempt:
            Attempt number that succeeds.

        maximum_attempts:
            Maximum retries.

    Returns:
        True if connection succeeds.
    """
    attempt = 1

    while attempt <= maximum_attempts:
        if attempt == success_on_attempt:
            break

        attempt += 1
    else:
        return False

    return True


def wait_for_service(
    ready_after: int,
    timeout: int,
) -> bool:
    """
    Simulate waiting for a service.

    Args:
        ready_after:
            Iteration when service becomes ready.

        timeout:
            Maximum wait iterations.

    Returns:
        True if service becomes available.
    """
    counter = 1

    while counter <= timeout:
        if counter == ready_after:
            break

        counter += 1
    else:
        return False

    return True


def first_divisible(
    numbers: list[int],
    divisor: int,
) -> int | None:
    """
    Return the first divisible number.

    Args:
        numbers:
            Input numbers.

        divisor:
            Divisor.

    Returns:
        First divisible number or None.
    """
    for number in numbers:
        if number % divisor == 0:
            return number
    else:
        return None


def validate_inventory(
    quantities: list[int],
) -> bool:
    """
    Validate inventory quantities.

    Every quantity must be positive.

    Args:
        quantities:
            Inventory values.

    Returns:
        True if inventory is valid.
    """
    for quantity in quantities:
        if quantity <= 0:
            break
    else:
        return True

    return False


def process_queue(
    queue: list[str],
    stop_value: str,
) -> list[str]:
    """
    Process queue until stop value.

    Args:
        queue:
            Queue items.

        stop_value:
            Processing stop marker.

    Returns:
        Processed items.
    """
    processed: list[str] = []

    for item in queue:
        if item == stop_value:
            break

        processed.append(item)

    return processed


def authenticate_user(
    usernames: list[str],
    target: str,
) -> bool:
    """
    Authenticate a user by username.

    Args:
        usernames:
            Available usernames.

        target:
            Username to authenticate.

    Returns:
        Authentication result.
    """
    for username in usernames:
        if username == target:
            break
    else:
        return False

    return True


__all__ = [
    "search_item",
    "find_employee",
    "is_prime",
    "login_attempts",
    "retry_connection",
    "wait_for_service",
    "first_divisible",
    "validate_inventory",
    "process_queue",
    "authenticate_user",
]