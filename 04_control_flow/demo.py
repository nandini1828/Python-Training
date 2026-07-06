"""
Demonstration script for the control_flow package.

Run this file to see examples of every concept covered in the
control_flow module.

Example:
    python demo.py
"""

from __future__ import annotations

from conditionals import (
    calculate_grade,
    check_number,
    classify_triangle,
    determine_discount,
    determine_temperature_status,
    employee_bonus,
    is_adult,
    loan_approval,
    shipping_charge,
)

from logical_operators import (
    can_access_admin_panel,
    can_access_resource,
    can_apply_for_job,
    can_drive,
    can_vote,
    contains_keyword,
    evaluate_login,
    has_permission,
    is_active_user,
    is_eligible_for_loan,
    operator_precedence_example,
    requires_manual_review,
    should_send_email,
)

from pattern_matching import (
    User,
    authenticate_user,
    calculator,
    classify_number,
    detect_file_type,
    determine_weekend,
    extract_coordinates,
    get_http_status_message,
    identify_collection,
    parse_api_response,
    parse_command,
)

from short_circuit import (
    cached_value_example,
    email_domain,
    first_non_empty,
    get_configuration,
    get_nested_value,
    get_username,
    positive_even_number,
    safe_length,
    safe_upper,
)

from ternary_operator import (
    absolute_value,
    determine_status,
    discount_percentage,
    employee_status,
    even_or_odd,
    file_permission,
    grade,
    login_message,
    maximum,
    minimum,
    pass_or_fail,
    salary_category,
    safe_username,
    traffic_signal,
)

from truthy_falsy import (
    Playlist,
    ShoppingCart,
    any_value_truthy,
    default_username,
    falsy_examples,
    first_available_value,
    get_truthiness,
    is_falsy,
    is_truthy,
    remove_falsy_values,
    truthy_examples,
)

from utils import (
    print_banner,
    print_result,
    print_subsection,
)


def demonstrate_conditionals() -> None:
    """Demonstrate conditional statements."""

    print_banner("Conditional Statements")

    print_result("Adult", is_adult(25))
    print_result("Number", check_number(-20))
    print_result("Grade", calculate_grade(91))
    print_result("Discount", determine_discount(7000, True))
    print_result("Temperature", determine_temperature_status(32))
    print_result("Loan", loan_approval(50000, 760, False))
    print_result("Shipping", shipping_charge(1500))
    print_result("Employee Bonus", employee_bonus(8, 5))
    print_result("Triangle", classify_triangle(3, 4, 5))


def demonstrate_truthy_falsy() -> None:
    """Demonstrate truthy and falsy values."""

    print_banner("Truthy & Falsy")

    print_result("Truthy", is_truthy([1, 2]))
    print_result("Falsy", is_falsy([]))
    print_result("Truthiness", get_truthiness(""))
    print_result("Default Username", default_username(None))
    print_result("First Available", first_available_value("", None, "Python"))
    print_result("Any Truthy", any_value_truthy([0, "", 10]))
    print_result(
        "Remove Falsy",
        remove_falsy_values([0, "", None, 5, "Python"]),
    )

    cart = ShoppingCart(["Keyboard"])
    playlist = Playlist(["Song A", "Song B"])

    print_result("Shopping Cart", bool(cart))
    print_result("Playlist", bool(playlist))
    print_result("Truthy Examples", truthy_examples())
    print_result("Falsy Examples", falsy_examples())


def demonstrate_logical_operators() -> None:
    """Demonstrate logical operators."""

    print_banner("Logical Operators")

    print_result("Admin", can_access_admin_panel(True, True))
    print_result("Vote", can_vote(21, True))
    print_result("Drive", can_drive(25, True))
    print_result("Loan", is_eligible_for_loan(80000, 760))
    print_result("Job", can_apply_for_job(1, True))
    print_result("Manual Review", requires_manual_review(150000, False))
    print_result("User Active", is_active_user(False, False))
    print_result("Send Email", should_send_email(True, True))
    print_result("Permission", has_permission("developer", {"write"}))
    print_result("Keyword", contains_keyword("Learn Python", "python"))
    print_result(
        "Precedence",
        operator_precedence_example(20, False, True),
    )
    print_result("Login", evaluate_login("admin", "python123"))
    print_result(
        "Resource",
        can_access_resource(True, False, True),
    )


def demonstrate_short_circuit() -> None:
    """Demonstrate short-circuit evaluation."""

    print_banner("Short Circuit Evaluation")

    print_result("Cache", cached_value_example(None))
    print_result("Upper", safe_upper("python"))
    print_result("Length", safe_length([1, 2, 3]))
    print_result("Username", get_username(None))
    print_result(
        "Configuration",
        get_configuration(None, "config.yaml", "default"),
    )
    print_result(
        "First Non Empty",
        first_non_empty("", None, "ChatGPT"),
    )
    print_result(
        "Nested Value",
        get_nested_value({"name": "Alice"}, "name"),
    )
    print_result(
        "Email Domain",
        email_domain("user@example.com"),
    )
    print_result(
        "Positive Even",
        positive_even_number(20),
    )


def demonstrate_ternary() -> None:
    """Demonstrate ternary operators."""

    print_banner("Ternary Operator")

    print_result("Status", determine_status(25))
    print_result("Absolute", absolute_value(-50))
    print_result("Maximum", maximum(10, 20))
    print_result("Minimum", minimum(10, 20))
    print_result("Even/Odd", even_or_odd(15))
    print_result("Pass", pass_or_fail(76))
    print_result("Login", login_message(True))
    print_result("Salary", salary_category(120000))
    print_result("Grade", grade(88))
    print_result("Discount", discount_percentage(True))
    print_result("Username", safe_username(""))
    print_result("Employee", employee_status(True))
    print_result("Permission", file_permission(False))
    print_result("Signal", traffic_signal("green"))


def demonstrate_pattern_matching() -> None:
    """Demonstrate structural pattern matching."""

    print_banner("Pattern Matching")

    print_result("HTTP", get_http_status_message(404))
    print_result("Weekend", determine_weekend("Sunday"))
    print_result("Number", classify_number(-10))
    print_result("Command", parse_command(["copy", "a.txt", "b.txt"]))
    print_result("Coordinates", extract_coordinates((10, 20)))
    print_result(
        "API",
        parse_api_response(
            {"status": "success", "data": "Loaded"},
        ),
    )

    admin = User("alice", "admin", True)

    print_result("User", authenticate_user(admin))
    print_result("Collection", identify_collection([1, 2, 3]))
    print_result("File", detect_file_type("README.md"))
    print_result("Calculator", calculator("+", 20, 30))


def main() -> None:
    """Run every demonstration."""

    print_banner("Python Control Flow Module")

    demonstrate_conditionals()

    demonstrate_truthy_falsy()

    demonstrate_logical_operators()

    demonstrate_short_circuit()

    demonstrate_ternary()

    demonstrate_pattern_matching()

    print_subsection("Demo Completed")


if __name__ == "__main__":
    main()