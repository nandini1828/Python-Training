"""
Operations related to while-else statements.
"""


def verify_pin(correct_pin: str, attempts: list[str]) -> bool:
    """Verify a PIN using while-else."""
    index = 0

    while index < len(attempts):
        if attempts[index] == correct_pin:
            return True
        index += 1
    else:
        return False


def search_number(numbers: list[int], target: int) -> bool:
    """Search for a number using while-else."""
    index = 0

    while index < len(numbers):
        if numbers[index] == target:
            return True
        index += 1
    else:
        return False


def countdown(number: int) -> int:
    """Return zero after counting down."""
    while number > 0:
        number -= 1
    else:
        return number


def password_attempts(correct_password: str, attempts: list[str]) -> bool:
    """Validate password attempts."""
    index = 0

    while index < len(attempts):
        if attempts[index] == correct_password:
            return True
        index += 1
    else:
        return False