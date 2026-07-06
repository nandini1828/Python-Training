"""
Examples demonstrating Python's structural pattern matching.

Python 3.10 introduced the ``match-case`` statement, which provides a
cleaner and more expressive alternative to long ``if-elif-else`` chains.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class User:
    """Represents a system user."""

    username: str
    role: str
    active: bool


def get_http_status_message(status_code: int) -> str:
    """Return an HTTP status message."""
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 204:
            return "No Content"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


def determine_weekend(day: str) -> bool:
    """Determine whether a day is a weekend."""
    match day.lower():
        case "saturday" | "sunday":
            return True
        case _:
            return False


def classify_number(number: int) -> str:
    """Classify a number."""
    match number:
        case value if value < 0:
            return "Negative"
        case 0:
            return "Zero"
        case value if value % 2 == 0:
            return "Positive Even"
        case _:
            return "Positive Odd"


def parse_command(command: list[str]) -> str:
    """Parse a command."""
    match command:
        case ["exit"]:
            return "Exit Application"

        case ["help"]:
            return "Display Help"

        case ["delete", filename]:
            return f"Delete '{filename}'"

        case ["copy", source, destination]:
            return f"Copy '{source}' -> '{destination}'"

        case _:
            return "Unknown Command"


def extract_coordinates(point: tuple[int, int]) -> str:
    """Describe coordinates."""
    match point:
        case (0, 0):
            return "Origin"

        case (0, y):
            return f"Y Axis ({y})"

        case (x, 0):
            return f"X Axis ({x})"

        case (x, y):
            return f"Point ({x}, {y})"


def parse_api_response(response: dict[str, Any]) -> str:
    """Parse API response."""
    match response:
        case {"status": "success", "data": data}:
            return f"Success ({data})"

        case {"status": "error", "message": message}:
            return f"Error ({message})"

        case _:
            return "Invalid Response"


def authenticate_user(user: User) -> str:
    """Authenticate user."""
    match user:
        case User(role="admin", active=True):
            return "Administrator Access"

        case User(role="manager", active=True):
            return "Manager Access"

        case User(active=False):
            return "Account Disabled"

        case User():
            return "Standard User"


def identify_collection(value: Any) -> str:
    """Identify common list patterns."""
    match value:
        case []:
            return "Empty List"

        case [item]:
            return f"Single Item ({item})"

        case [first, second]:
            return f"Two Items ({first}, {second})"

        case [first, *rest]:
            return f"Starts With {first}, Remaining {len(rest)}"

        case _:
            return "Unknown Collection"


def detect_file_type(filename: str) -> str:
    """Detect file type."""

    if "." not in filename:
        return "Unknown File Type"

    extension = filename.rsplit(".", 1)[1].lower()

    match extension:
        case "pdf":
            return "PDF Document"

        case "jpg" | "jpeg" | "png":
            return "Image"

        case "py":
            return "Python Source"

        case "md":
            return "Markdown"

        case _:
            return "Unknown File Type"


def calculator(operation: str, left: float, right: float) -> float:
    """Simple calculator."""

    match operation:
        case "+":
            return left + right

        case "-":
            return left - right

        case "*":
            return left * right

        case "/":
            if right == 0:
                raise ValueError("Division by zero is not allowed.")
            return left / right

        case _:
            raise ValueError(f"Unsupported operation: {operation}")


__all__ = [
    "User",
    "get_http_status_message",
    "determine_weekend",
    "classify_number",
    "parse_command",
    "extract_coordinates",
    "parse_api_response",
    "authenticate_user",
    "identify_collection",
    "detect_file_type",
    "calculator",
]