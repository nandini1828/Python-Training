"""
Basic if-elif-else examples.
"""


def classify_number(number: int) -> str:
    """
    Classifies a number as Positive, Negative, or Zero.

    Parameters
    ----------
    number : int
        Number to classify.

    Returns
    -------
    str
        Classification result.
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"


def check_pass_status(score: int) -> str:
    """
    Returns Pass if score >= 35, otherwise Fail.
    """
    if score >= 35:
        return "Pass"
    return "Fail"