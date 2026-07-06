"""
utils.py

Reusable utility functions demonstrating Python's
Structural Pattern Matching (match-case).
"""


def get_day(day: int) -> str:
    """Return the day of the week."""
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid Day"


def calculate(a: float, b: float, operator: str):
    """Perform arithmetic operations."""
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "Division by Zero"
        case _:
            return "Invalid Operator"


def get_http_status(code: int) -> str:
    """Return HTTP status description."""
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


def get_role_permissions(role: str) -> str:
    """Return permissions based on user role."""
    match role.lower():
        case "admin":
            return "Full Access"
        case "manager":
            return "Manager Access"
        case "employee":
            return "Employee Access"
        case "guest":
            return "Limited Access"
        case _:
            return "Unknown Role"


def get_grade_remark(grade: str) -> str:
    """Return remark for a grade."""
    match grade.upper():
        case "A" | "A+":
            return "Excellent"
        case "B" | "B+":
            return "Very Good"
        case "C":
            return "Good"
        case "D":
            return "Average"
        case _:
            return "Fail"


def classify_point(point: tuple) -> str:
    """Classify a point in 2D space."""
    match point:
        case (0, 0):
            return "Origin"
        case (0, _):
            return "Y-Axis"
        case (_, 0):
            return "X-Axis"
        case (_, _):
            return "General Point"


def list_information(values: list) -> str:
    """Return information about a list."""
    match values:
        case []:
            return "Empty List"
        case [_]:
            return "Single Element"
        case [_, _]:
            return "Two Elements"
        case [_, *_]:
            return "Multiple Elements"


def student_information(student: dict) -> str:
    """Extract student information."""
    match student:
        case {"name": name, "age": age}:
            return f"{name} ({age})"
        case _:
            return "Invalid Student"


def age_group(age: int) -> str:
    """Return age category using guards."""
    match age:
        case age if age < 18:
            return "Minor"
        case age if age < 60:
            return "Adult"
        case _:
            return "Senior Citizen"


def execute_command(command: str) -> str:
    """Execute a simple command."""
    match command.lower():
        case "start":
            return "Application Started"
        case "stop":
            return "Application Stopped"
        case "restart":
            return "Application Restarted"
        case "exit":
            return "Application Closed"
        case _:
            return "Unknown Command"