"""
Logical operator examples: and, or, not.
"""


def evaluate_logical_operations(first_condition: bool, second_condition: bool) -> dict[str, bool]:
    """
    Evaluates logical operations for two boolean inputs.

    Returns
    -------
    dict[str, bool]
        Results for and, or, and not.
    """
    return {
        "and_result": first_condition and second_condition,
        "or_result": first_condition or second_condition,
        "not_first": not first_condition,
        "not_second": not second_condition,
    }


def can_access_system(is_admin: bool, is_active: bool) -> bool:
    """
    Returns True only if the user is both admin and active.
    """
    return is_admin and is_active