"""
Tests for data inspection.
"""

from utilities.dataset_loader import load_employees


def test_dataframe_shape():
    df = load_employees()

    assert df.shape == (10, 8)


def test_column_names():
    df = load_employees()

    assert "Salary" in df.columns
    assert "Department" in df.columns


def test_no_missing_values():
    df = load_employees()

    assert df.isnull().sum().sum() == 0


def test_describe():
    df = load_employees()

    description = df.describe()

    assert "Salary" in description.columns


def test_unique_departments():
    df = load_employees()

    assert df["Department"].nunique() == 5