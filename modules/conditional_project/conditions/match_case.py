"""
Examples of match-case.
"""


def day_name(day: int) -> str:

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


def calculator(a: int, b: int, operator: str):

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


def traffic_signal(color: str):

    match color.lower():
        case "red":
            return "Stop"
        case "yellow":
            return "Ready"
        case "green":
            return "Go"
        case _:
            return "Unknown Signal"