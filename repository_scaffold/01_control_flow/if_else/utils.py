"""
utils.py

Reusable utility functions demonstrating the use of
if-elif-else statements.

These functions are designed to be imported by other
modules and tested independently.
"""


def is_adult(age: int) -> bool:
    """
    Check whether a person is an adult.

    Args:
        age (int): Age of the person.

    Returns:
        bool: True if age is 18 or above.
    """
    return age >= 18


def can_vote(age: int, citizen: bool) -> bool:
    """
    Determine voting eligibility.

    Args:
        age (int): Person's age.
        citizen (bool): Citizenship status.

    Returns:
        bool
    """
    return age >= 18 and citizen


def calculate_grade(marks: int) -> str:
    """
    Calculate student grade.

    Args:
        marks (int): Marks obtained.

    Returns:
        str: Grade
    """

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    return "Fail"


def largest_number(a: float, b: float):
    """
    Return the larger of two numbers.
    """

    if a >= b:
        return a

    return b


def smallest_number(a: float, b: float):
    """
    Return the smaller of two numbers.
    """

    if a <= b:
        return a

    return b


def check_leap_year(year: int) -> bool:
    """
    Check whether a year is a leap year.
    """

    return (year % 400 == 0) or (
        year % 4 == 0 and year % 100 != 0
    )


def validate_login(
    username: str,
    password: str,
    valid_username: str,
    valid_password: str,
) -> bool:
    """
    Validate user credentials.
    """

    return (
        username == valid_username
        and password == valid_password
    )


def calculate_discount(
    amount: float,
) -> int:
    """
    Calculate discount percentage.

    Returns:
        int: Discount percentage
    """

    if amount >= 5000:
        return 25

    elif amount >= 3000:
        return 20

    elif amount >= 1000:
        return 10

    return 0


def employee_bonus(rating: int) -> int:
    """
    Calculate employee bonus.

    Returns:
        Bonus amount.
    """

    if rating == 5:
        return 50000

    elif rating == 4:
        return 30000

    elif rating == 3:
        return 15000

    return 5000


def traffic_signal(signal: str) -> str:
    """
    Return action based on traffic signal.
    """

    signal = signal.lower()

    if signal == "red":
        return "STOP"

    elif signal == "yellow":
        return "READY"

    elif signal == "green":
        return "GO"

    return "INVALID SIGNAL"


def weather_advice(weather: str) -> str:
    """
    Return weather advice.
    """

    weather = weather.lower()

    if weather == "sunny":
        return "Go Outside"

    elif weather == "rainy":
        return "Carry an Umbrella"

    elif weather == "cloudy":
        return "Pleasant Weather"

    elif weather == "snow":
        return "Wear Warm Clothes"

    return "Unknown Weather"


def check_number(number: float) -> str:
    """
    Identify whether a number is
    Positive, Negative or Zero.
    """

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    return "Zero"


def even_or_odd(number: int) -> str:
    """
    Check whether a number is even or odd.
    """

    if number % 2 == 0:
        return "Even"

    return "Odd"


def pass_or_fail(marks: int) -> str:
    """
    Determine pass or fail.
    """

    if marks >= 40:
        return "Pass"

    return "Fail"