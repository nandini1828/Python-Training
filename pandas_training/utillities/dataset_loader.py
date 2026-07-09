"""
Utility functions for loading datasets.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_employees():
    """Load employees dataset."""
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def load_students():
    """Load students dataset."""
    return pd.read_csv(DATA_FOLDER / "students.csv")


def load_sales():
    """Load sales dataset."""
    return pd.read_csv(DATA_FOLDER / "sales.csv")


def load_customers():
    """Load customers dataset."""
    return pd.read_csv(DATA_FOLDER / "customers.csv")


def load_employees_missing():
    """Load employees dataset containing missing values."""
    return pd.read_csv(DATA_FOLDER / "employees_missing.csv")


def load_department_bonus():
    """Load department bonus dataset."""
    return pd.read_csv(DATA_FOLDER / "department_bonus.csv")


def load_new_employees():
    """Load new employees dataset."""
    return pd.read_csv(DATA_FOLDER / "new_employees.csv")


def load_csv(file_name):
    """
    Generic CSV loader.

    Example:
        df = load_csv("employees.csv")
    """

    return pd.read_csv(DATA_FOLDER / file_name)