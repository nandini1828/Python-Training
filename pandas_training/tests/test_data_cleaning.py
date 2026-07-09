"""
Tests for data cleaning.
"""

from utilities.dataset_loader import (
    load_employees,
    load_employees_missing,
)


def test_missing_values():
    df = load_employees_missing()

    assert df.isnull().sum().sum() > 0


def test_fillna():
    df = load_employees_missing()

    filled = df.fillna("Unknown")

    assert filled.isnull().sum().sum() == 0


def test_drop_duplicates():
    df = load_employees_missing()

    cleaned = df.drop_duplicates()

    assert len(cleaned) == 9


def test_add_column():
    df = load_employees()

    df["Bonus"] = df["Salary"] * 0.10

    assert "Bonus" in df.columns


def test_astype():
    df = load_employees()

    df["Salary"] = df["Salary"].astype(float)

    assert str(df["Salary"].dtype) == "float64"