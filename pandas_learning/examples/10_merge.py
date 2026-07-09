"""
10_merge.py

Learning Objectives
-------------------
1. Inner Join
2. Left Join
3. Right Join
4. Outer Join
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

EMPLOYEE_FILE = Path("datasets/employees.csv")
DEPARTMENT_FILE = Path("datasets/departments.csv")


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    employees = pd.read_csv(EMPLOYEE_FILE)
    departments = pd.read_csv(DEPARTMENT_FILE)

    return employees, departments


def demonstrate_merge(
    employees: pd.DataFrame,
    departments: pd.DataFrame,
) -> None:

    joins = ["inner", "left", "right", "outer"]

    for join in joins:

        print("\n" + "=" * 70)
        print(join.upper(), "JOIN")
        print("=" * 70)

        merged = pd.merge(
            employees,
            departments,
            on="department",
            how=join,
        )

        print(merged.head())


def main() -> None:
    employees, departments = load_data()

    demonstrate_merge(
        employees,
        departments,
    )


if __name__ == "__main__":
    main()