"""
match-case examples (Python 3.10+).
"""

import sys

if sys.version_info < (3, 10):
    raise RuntimeError("This script requires Python 3.10 or later")


def get_day_category(day: str) -> str:
    """
    Categorizes a day using match-case.
    """
    match day.lower():
        case "monday":
            return "Start of Week"
        case "friday":
            return "Almost Weekend"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Regular Day"


def traffic_signal_action(signal: str) -> str:
    """
    Returns action based on traffic signal color.
    """
    match signal.lower():
        case "red":
            return "Stop"
        case "yellow":
            return "Get Ready"
        case "green":
            return "Go"
        case _:
            return "Invalid Signal"