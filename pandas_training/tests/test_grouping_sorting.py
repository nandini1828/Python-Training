"""
Tests for grouping and sorting.
"""

import pandas as pd

from utilities.dataset_loader import (
    load_employees,
    load_department_bonus,
    load_new_employees,
)


def test_sort_salary():
    df = load_employees()

    sorted_df = df.sort_values("Salary")

    assert sorted_df.iloc[0]["Salary"] == 45000


def test_groupby_mean():
    df = load_employees()

    grouped = df.groupby("Department")["Salary"].mean()

    assert "IT" in grouped.index


def test_merge():
    emp = load_employees()

    bonus = load_department_bonus()

    merged = pd.merge(
        emp,
        bonus,
        on="Department",
    )

    assert "BonusPercentage" in merged.columns


def test_concat():
    emp = load_employees()

    new = load_new_employees()

    result = pd.concat(
        [emp, new],
        ignore_index=True,
    )

    assert len(result) == 15


def test_sort_index():
    df = load_employees()

    shuffled = df.sample(frac=1)

    sorted_df = shuffled.sort_index()

    assert sorted_df.index.is_monotonic_increasing