"""
Tests for selection and filtering.
"""

from utilities.dataset_loader import load_employees


def test_select_single_column():
    df = load_employees()

    names = df["Name"]

    assert len(names) == 10


def test_multiple_columns():
    df = load_employees()

    selected = df[
        ["Name", "Salary"]
    ]

    assert selected.shape == (10, 2)


def test_filter_salary():
    df = load_employees()

    result = df[df["Salary"] > 60000]

    assert all(result["Salary"] > 60000)


def test_filter_city():
    df = load_employees()

    result = df[df["City"] == "Hyderabad"]

    assert len(result) == 3


def test_multiple_conditions():
    df = load_employees()

    result = df[
        (df["Department"] == "IT")
        &
        (df["Salary"] > 45000)
    ]

    assert len(result) > 0