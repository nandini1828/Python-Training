"""
demo.py

Practical demonstrations of Python Ternary Operator.
"""


def basic_demo():
    age = 20
    result = "Adult" if age >= 18 else "Minor"
    print(result)


def even_odd():
    number = 17
    result = "Even" if number % 2 == 0 else "Odd"
    print(result)


def largest_number():
    a = 15
    b = 22
    print(a if a > b else b)


def positive_negative():
    number = -5
    print("Positive" if number > 0 else "Negative")


def pass_fail():
    marks = 76
    print("Pass" if marks >= 40 else "Fail")


def login():
    authenticated = True
    print("Welcome" if authenticated else "Access Denied")


def weather():
    raining = False
    print("Go Outside" if not raining else "Stay Inside")


def scholarship():
    marks = 95
    print("Eligible" if marks >= 90 else "Not Eligible")


def employee_bonus():
    rating = 5
    print(50000 if rating == 5 else 10000)


def main():
    print("=" * 60)
    print("TERNARY OPERATOR DEMONSTRATIONS")
    print("=" * 60)

    basic_demo()
    even_odd()
    largest_number()
    positive_negative()
    pass_fail()
    login()
    weather()
    scholarship()
    employee_bonus()

    print("\nCompleted Successfully.")


if __name__ == "__main__":
    main()