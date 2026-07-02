"""Examples that demonstrate conditional branching in Python."""

from __future__ import annotations


def grade_student(score: int) -> str:
    """Return a letter grade for a numeric score.

    Args:
        score: A numeric student score between 0 and 100.

    Returns:
        The corresponding grade category.
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def validate_login(username: str, password: str) -> str:
    """Validate a login form using simple conditional logic.

    Args:
        username: The submitted username.
        password: The submitted password.

    Returns:
        A friendly success or error message.
    """
    if not username:
        return "Username is required."
    if not password:
        return "Password is required."
    if username == "admin" and password == "secret123":
        return "Login successful."
    return "Invalid credentials."


def simulate_atm_menu(balance: float, choice: str) -> str:
    """Show a small ATM-style menu using nested conditionals.

    Args:
        balance: The current account balance.
        choice: The selected menu action.

    Returns:
        A descriptive message for the chosen action.
    """
    if choice == "balance":
        return f"Your balance is ${balance:.2f}."
    if choice == "deposit":
        return "Deposit service is available."
    if choice == "withdraw":
        if balance >= 50:
            return "Withdrawal approved."
        return "Insufficient funds."
    return "Unknown option."
