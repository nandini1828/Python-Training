"""
main.py

Entry point for Python Control Flow Mastery.

Topics Covered:
- if-elif-else
- Truthy & Falsy
- Logical Operators
- Short-Circuit Evaluation
- Ternary Operator
- Match-Case
"""

import argparse

from conditionals import (
    IfElseExamples,
    TruthyFalsyExamples,
    LogicalOperatorExamples,
    ShortCircuitExamples,
    TernaryExamples,
    MatchCaseExamples
)


def demonstrate_if_else() -> None:
    """Demonstrates if-elif-else examples."""

    print("\n" + "=" * 60)
    print("IF - ELIF - ELSE")
    print("=" * 60)

    print("Positive Check :", IfElseExamples.check_number(10))
    print("Age Check      :", IfElseExamples.check_age(22))
    print("Grade          :", IfElseExamples.calculate_grade(91))
    print("Largest        :", IfElseExamples.find_largest(20, 40))
    print("Even / Odd     :", IfElseExamples.check_even_or_odd(15))
    print("Password       :", IfElseExamples.validate_password("python123"))
    print("Discount       :", IfElseExamples.check_discount(7000))
    print(
        "Login          :",
        IfElseExamples.login_status(
            "admin",
            "admin123"
        )
    )


def demonstrate_truthy_falsy() -> None:
    """Demonstrates Truthy and Falsy values."""

    print("\n" + "=" * 60)
    print("TRUTHY & FALSY")
    print("=" * 60)

    print("Truthy List    :", TruthyFalsyExamples.is_truthy([1, 2]))
    print("Falsy List     :", TruthyFalsyExamples.is_falsy([]))
    print("Collection     :", TruthyFalsyExamples.check_collection([]))
    print("Username       :", TruthyFalsyExamples.check_username("Bhavya"))
    print("Optional Value :", TruthyFalsyExamples.check_optional_value(None))
    print("API Response   :", TruthyFalsyExamples.check_api_response({}))
    print(
        "Login          :",
        TruthyFalsyExamples.validate_login(
            "admin",
            "password"
        )
    )
    print("Number Check   :", TruthyFalsyExamples.check_number(0))
    print("Default Name   :", TruthyFalsyExamples.get_default_name(""))
    print("Falsy Values   :", TruthyFalsyExamples.demonstrate_falsy_values())


def demonstrate_logical_operators() -> None:
    """Demonstrates logical operators."""

    print("\n" + "=" * 60)
    print("LOGICAL OPERATORS")
    print("=" * 60)

    print("Can Vote       :", LogicalOperatorExamples.can_vote(22, True))
    print(
        "Login          :",
        LogicalOperatorExamples.login(
            "admin",
            "admin123"
        )
    )
    print(
        "Access         :",
        LogicalOperatorExamples.has_access(
            False,
            True
        )
    )
    print(
        "Email          :",
        LogicalOperatorExamples.validate_email(
            "abc@gmail.com"
        )
    )
    print(
        "Store Open     :",
        LogicalOperatorExamples.is_store_open(
            False,
            False
        )
    )
    print(
        "Positive Even  :",
        LogicalOperatorExamples.is_even_positive(
            12
        )
    )
    print(
        "Loan Eligible  :",
        LogicalOperatorExamples.can_apply_for_loan(
            80000,
            760
        )
    )
    print(
        "Student Passed :",
        LogicalOperatorExamples.student_passed(
            60,
            70
        )
    )
    print(
        "Movie Access   :",
        LogicalOperatorExamples.can_watch_movie(
            16,
            True
        )
    )
    print(
        "Account Active :",
        LogicalOperatorExamples.account_active(
            False
        )
    )


def demonstrate_short_circuit() -> None:
    """Demonstrates short-circuit evaluation."""

    print("\n" + "=" * 60)
    print("SHORT CIRCUIT EVALUATION")
    print("=" * 60)

    print("Using AND      :", ShortCircuitExamples.using_and(20, True))
    print("Using OR       :", ShortCircuitExamples.using_or(""))
    print("Safe Division  :", ShortCircuitExamples.safe_division(20, 5))
    print("Default Value  :", ShortCircuitExamples.default_discount(0))
    print(
        "Portal Access  :",
        ShortCircuitExamples.can_access_portal(
            True,
            True
        )
    )
    print(
        "Display Name   :",
        ShortCircuitExamples.get_display_name("")
    )
    print(
        "Has Data       :",
        ShortCircuitExamples.has_data(
            [1, 2, 3]
        )
    )
    print(
        "First Item     :",
        ShortCircuitExamples.get_first_item(
            [10, 20, 30]
        )
    )


def demonstrate_ternary() -> None:
    """Demonstrates ternary operator."""

    print("\n" + "=" * 60)
    print("TERNARY OPERATOR")
    print("=" * 60)

    print("Even/Odd       :", TernaryExamples.even_or_odd(10))
    print("Pass/Fail      :", TernaryExamples.pass_or_fail(65))
    print("Largest        :", TernaryExamples.largest(40, 60))
    print("Voting         :", TernaryExamples.voting_status(22))
    print("Login          :", TernaryExamples.login_message(True))
    print("Maximum        :", TernaryExamples.maximum(5, 15, 10))
    print("Discount       :", TernaryExamples.discount(7000))


def demonstrate_match_case() -> None:
    """Demonstrates match-case."""

    print("\n" + "=" * 60)
    print("MATCH CASE")
    print("=" * 60)

    print("Day            :", MatchCaseExamples.day_name(1))
    print("Signal         :", MatchCaseExamples.traffic_signal("green"))
    print("Calculator     :", MatchCaseExamples.calculator(20, 10, "+"))
    print("HTTP Status    :", MatchCaseExamples.http_status(200))
    print("Grade          :", MatchCaseExamples.grade("A"))
    print("Role           :", MatchCaseExamples.employee_role("admin"))


def run_all() -> None:
    """Runs all demonstrations."""

    demonstrate_if_else()
    demonstrate_truthy_falsy()
    demonstrate_logical_operators()
    demonstrate_short_circuit()
    demonstrate_ternary()
    demonstrate_match_case()


def main() -> None:
    """
    Parses command-line arguments
    and executes selected module.
    """

    parser = argparse.ArgumentParser(
        description="Python Control Flow Mastery"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "ifelse",
            "truthy",
            "logical",
            "shortcircuit",
            "ternary",
            "match"
        ],
        help="Run a specific topic."
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "ifelse":
        demonstrate_if_else()

    elif args.section == "truthy":
        demonstrate_truthy_falsy()

    elif args.section == "logical":
        demonstrate_logical_operators()

    elif args.section == "shortcircuit":
        demonstrate_short_circuit()

    elif args.section == "ternary":
        demonstrate_ternary()

    elif args.section == "match":
        demonstrate_match_case()

    print("\nProject Executed Successfully")


if __name__ == "__main__":
    main()