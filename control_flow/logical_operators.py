"""
Examples demonstrating Python logical operators.

Topics covered:
- and
- or
- not
- Operator precedence
- Membership checks
- Identity checks
- Real-world decision making

Author: Python Training
"""

from __future__ import annotations


def can_access_admin_panel(
    is_logged_in: bool,
    is_admin: bool,
) -> bool:
    """
    Determine whether a user can access the admin panel.

    Args:
        is_logged_in:
            Whether the user is authenticated.
        is_admin:
            Whether the user has administrator privileges.

    Returns:
        True if access is granted.
    """
    return is_logged_in and is_admin


def can_vote(
    age: int,
    is_citizen: bool,
) -> bool:
    """
    Determine whether a person is eligible to vote.

    Args:
        age:
            Person's age.
        is_citizen:
            Citizenship status.

    Returns:
        True if eligible.
    """
    return age >= 18 and is_citizen


def can_drive(
    age: int,
    has_license: bool,
) -> bool:
    """
    Determine whether a person can legally drive.

    Args:
        age:
            Driver's age.
        has_license:
            Driving license status.

    Returns:
        True if the person can drive.
    """
    return age >= 18 and has_license


def is_eligible_for_loan(
    salary: float,
    credit_score: int,
) -> bool:
    """
    Determine whether a loan can be approved.

    Args:
        salary:
            Monthly salary.
        credit_score:
            Credit score.

    Returns:
        True if eligible.
    """
    return salary >= 30_000 and credit_score >= 700


def can_apply_for_job(
    experience: int,
    degree: bool,
) -> bool:
    """
    Determine whether a candidate can apply.

    Args:
        experience:
            Years of experience.
        degree:
            Whether the candidate has a degree.

    Returns:
        True if requirements are satisfied.
    """
    return experience >= 2 or degree


def requires_manual_review(
    amount: float,
    is_blacklisted: bool,
) -> bool:
    """
    Determine whether a transaction requires manual review.

    Args:
        amount:
            Transaction amount.
        is_blacklisted:
            Blacklist status.

    Returns:
        True if manual review is required.
    """
    return amount > 100_000 or is_blacklisted


def is_active_user(
    is_deleted: bool,
    is_blocked: bool,
) -> bool:
    """
    Determine whether a user account is active.

    Args:
        is_deleted:
            Account deletion status.
        is_blocked:
            Account blocked status.

    Returns:
        True if the account is active.
    """
    return not is_deleted and not is_blocked


def should_send_email(
    email_verified: bool,
    marketing_opt_in: bool,
) -> bool:
    """
    Determine whether a marketing email should be sent.

    Args:
        email_verified:
            Email verification status.
        marketing_opt_in:
            Marketing subscription status.

    Returns:
        True if the email should be sent.
    """
    return email_verified and marketing_opt_in


def has_permission(
    role: str,
    permissions: set[str],
) -> bool:
    """
    Determine whether a user has write permission.

    Args:
        role:
            User role.
        permissions:
            Assigned permissions.

    Returns:
        True if permission exists.
    """
    return role == "admin" or "write" in permissions


def contains_keyword(
    text: str,
    keyword: str,
) -> bool:
    """
    Check whether a keyword exists inside text.

    Args:
        text:
            Input text.
        keyword:
            Search keyword.

    Returns:
        True if found.
    """
    return keyword.lower() in text.lower()


def is_same_object(
    first: object,
    second: object,
) -> bool:
    """
    Determine whether two references point to the same object.

    Args:
        first:
            First object.
        second:
            Second object.

    Returns:
        True if both references are identical.
    """
    return first is second


def is_not_none(value: object | None) -> bool:
    """
    Check whether a value is not None.

    Args:
        value:
            Object to check.

    Returns:
        True if value is not None.
    """
    return value is not None


def operator_precedence_example(
    age: int,
    is_admin: bool,
    is_verified: bool,
) -> bool:
    """
    Demonstrate logical operator precedence.

    In Python:
        not > and > or

    Equivalent expression:

        (age >= 18 and is_verified) or is_admin

    Args:
        age:
            User age.
        is_admin:
            Administrator status.
        is_verified:
            Verification status.

    Returns:
        Boolean result.
    """
    return age >= 18 and is_verified or is_admin


def evaluate_login(
    username: str,
    password: str,
) -> bool:
    """
    Simulate a login check.

    Args:
        username:
            Username.
        password:
            Password.

    Returns:
        True if credentials match.
    """
    return username == "admin" and password == "python123"


def can_access_resource(
    authenticated: bool,
    subscription_active: bool,
    trial_active: bool,
) -> bool:
    """
    Determine access to a protected resource.

    Args:
        authenticated:
            Authentication status.
        subscription_active:
            Subscription status.
        trial_active:
            Trial status.

    Returns:
        True if access should be granted.
    """
    return authenticated and (
        subscription_active or trial_active
    )


__all__ = [
    "can_access_admin_panel",
    "can_vote",
    "can_drive",
    "is_eligible_for_loan",
    "can_apply_for_job",
    "requires_manual_review",
    "is_active_user",
    "should_send_email",
    "has_permission",
    "contains_keyword",
    "is_same_object",
    "is_not_none",
    "operator_precedence_example",
    "evaluate_login",
    "can_access_resource",
]