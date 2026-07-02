"""
match_case.py

Demonstrates Python Match-Case Statement.

Topics Covered:
- Structural Pattern Matching
- match-case
"""


class MatchCaseExamples:
    """
    Utility class demonstrating
    Python match-case.
    """

    @staticmethod
    def day_name(day: int) -> str:
        """
        Returns weekday name.
        """

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

    @staticmethod
    def traffic_signal(color: str) -> str:
        """
        Returns action for signal.
        """

        match color.lower():

            case "red":
                return "Stop"

            case "yellow":
                return "Ready"

            case "green":
                return "Go"

            case _:
                return "Invalid Signal"

    @staticmethod
    def calculator(
        first: int,
        second: int,
        operator: str
    ):

        """
        Performs simple calculations.
        """

        match operator:

            case "+":
                return first + second

            case "-":
                return first - second

            case "*":
                return first * second

            case "/":
                if second == 0:
                    return "Division by Zero"

                return first / second

            case _:
                return "Invalid Operator"

    @staticmethod
    def http_status(code: int) -> str:
        """
        Returns HTTP status.
        """

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

    @staticmethod
    def grade(grade: str) -> str:
        """
        Returns grade description.
        """

        match grade.upper():

            case "A":
                return "Excellent"

            case "B":
                return "Very Good"

            case "C":
                return "Good"

            case "D":
                return "Average"

            case "F":
                return "Fail"

            case _:
                return "Invalid Grade"

    @staticmethod
    def employee_role(role: str) -> str:
        """
        Returns employee permissions.
        """

        match role.lower():

            case "admin":
                return "Full Access"

            case "manager":
                return "Manager Access"

            case "employee":
                return "Limited Access"

            case "guest":
                return "Read Only"

            case _:
                return "Invalid Role"