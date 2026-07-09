"""
advanced.py

Enterprise Pandas Project
=========================

Topics Covered
--------------

✓ Reading Multiple CSV Files
✓ Data Validation
✓ Data Cleaning
✓ Merge
✓ Concat
✓ DateTime Operations
✓ Aggregation
✓ Ranking
✓ Reporting

Datasets

datasets/
    employees.csv
    departments.csv
    sales.csv
    ecommerce.csv

Run

python solutions/advanced.py
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict

import pandas as pd

# =============================================================================
# Configuration
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# =============================================================================
# Dataset Paths
# =============================================================================

DATA_DIR = Path("datasets")

EMPLOYEE_FILE = DATA_DIR / "employees.csv"
DEPARTMENT_FILE = DATA_DIR / "departments.csv"
SALES_FILE = DATA_DIR / "sales.csv"
ECOMMERCE_FILE = DATA_DIR / "ecommerce.csv"

OUTPUT_DIR = Path("reports")
OUTPUT_DIR.mkdir(exist_ok=True)

# =============================================================================
# Utility Functions
# =============================================================================


def print_header(title: str) -> None:
    """Print formatted section headers."""

    print("\n")
    print("=" * 90)
    print(title)
    print("=" * 90)


def validate_file(path: Path) -> None:
    """
    Validate dataset exists.
    """

    if not path.exists():
        raise FileNotFoundError(
            f"Missing dataset : {path}"
        )


def load_csv(path: Path) -> pd.DataFrame:
    """
    Read CSV.
    """

    validate_file(path)

    logger.info("Loading %s", path.name)

    return pd.read_csv(path)


# =============================================================================
# Load All Datasets
# =============================================================================


def load_datasets() -> Dict[str, pd.DataFrame]:
    """
    Load every dataset.
    """

    datasets = {
        "employees": load_csv(EMPLOYEE_FILE),
        "departments": load_csv(DEPARTMENT_FILE),
        "sales": load_csv(SALES_FILE),
        "ecommerce": load_csv(ECOMMERCE_FILE),
    }

    logger.info("Datasets Loaded Successfully")

    return datasets


# =============================================================================
# Validation
# =============================================================================


def validate_dataframe(
    name: str,
    df: pd.DataFrame,
) -> None:
    """
    Validate dataframe.
    """

    print_header(f"{name.upper()} VALIDATION")

    print("Rows")
    print(len(df))

    print("\nColumns")
    print(len(df.columns))

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nData Types")
    print(df.dtypes)


def validate_all(
    datasets: Dict[str, pd.DataFrame],
) -> None:
    """
    Validate every dataset.
    """

    for name, dataframe in datasets.items():
        validate_dataframe(
            name,
            dataframe,
        )


# =============================================================================
# Generic Report Functions
# =============================================================================


def dataset_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create dataset summary.
    """

    summary = pd.DataFrame(
        {
            "Metric": [
                "Rows",
                "Columns",
                "Missing Values",
                "Duplicate Rows",
            ],
            "Value": [
                len(df),
                len(df.columns),
                int(df.isnull().sum().sum()),
                int(df.duplicated().sum()),
            ],
        }
    )

    return summary


def export_report(
    dataframe: pd.DataFrame,
    filename: str,
) -> None:
    """
    Export report.
    """

    output = OUTPUT_DIR / filename

    dataframe.to_csv(
        output,
        index=False,
    )

    logger.info(
        "Report exported : %s",
        output,
    )


# =============================================================================
# Overview Reports
# =============================================================================


def generate_overview_reports(
    datasets: Dict[str, pd.DataFrame],
) -> None:
    """
    Export overview of every dataset.
    """

    print_header("GENERATING OVERVIEW REPORTS")

    for name, dataframe in datasets.items():

        summary = dataset_summary(dataframe)

        export_report(
            summary,
            f"{name}_summary.csv",
        )


# =============================================================================
# Main (Temporary)
# =============================================================================
def main() -> None:
    """
    Entry point.
    """

    logger.info("Starting Enterprise Analytics Project")

    datasets = load_datasets()

    validate_all(datasets)

    generate_overview_reports(datasets)

    run_employee_analytics(datasets)

    logger.info("Employee Analytics Completed")


# =============================================================================
# Employee Analytics
# =============================================================================


def employee_overview(df: pd.DataFrame) -> None:
    """
    Display basic employee statistics.
    """

    print_header("EMPLOYEE OVERVIEW")

    print(f"Total Employees : {len(df)}")
    print(f"Departments     : {df['department'].nunique()}")
    print(f"Cities          : {df['city'].nunique()}")

    print("\nSalary Statistics")

    print(f"Average Salary : {df['salary'].mean():,.2f}")
    print(f"Maximum Salary : {df['salary'].max():,.2f}")
    print(f"Minimum Salary : {df['salary'].min():,.2f}")

    print("\nAge Statistics")

    print(df["age"].describe())


# =============================================================================
# Department Analysis
# =============================================================================


def department_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Department summary report.
    """

    print_header("DEPARTMENT SUMMARY")

    summary = (
        df.groupby("department")
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
            minimum_salary=("salary", "min"),
            maximum_salary=("salary", "max"),
            average_age=("age", "mean"),
            average_rating=("performance_rating", "mean"),
        )
        .round(2)
        .reset_index()
    )

    print(summary)

    return summary


# =============================================================================
# City Analysis
# =============================================================================


def city_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Employee count by city.
    """

    print_header("CITY SUMMARY")

    result = (
        df.groupby("city")
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
        )
        .sort_values(
            by="employee_count",
            ascending=False,
        )
        .round(2)
        .reset_index()
    )

    print(result)

    return result


# =============================================================================
# Top Employees
# =============================================================================


def top_paid_employees(
    df: pd.DataFrame,
    limit: int = 5,
) -> pd.DataFrame:
    """
    Highest paid employees.
    """

    print_header("TOP PAID EMPLOYEES")

    result = (
        df.nlargest(
            limit,
            "salary",
        )[
            [
                "first_name",
                "last_name",
                "department",
                "salary",
            ]
        ]
    )

    print(result)

    return result


# =============================================================================
# Performance Analysis
# =============================================================================


def performance_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Department performance report.
    """

    print_header("PERFORMANCE SUMMARY")

    result = (
        df.groupby("department")
        .agg(
            average_rating=(
                "performance_rating",
                "mean",
            ),
            highest_rating=(
                "performance_rating",
                "max",
            ),
            lowest_rating=(
                "performance_rating",
                "min",
            ),
        )
        .round(2)
        .reset_index()
    )

    print(result)

    return result


# =============================================================================
# Salary Ranking
# =============================================================================


def salary_ranking(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Rank employees by salary.
    """

    print_header("SALARY RANKING")

    ranked = df.copy()

    ranked["salary_rank"] = ranked["salary"].rank(
        ascending=False,
        method="dense",
    )

    ranked = ranked.sort_values("salary_rank")

    print(
        ranked[
            [
                "salary_rank",
                "first_name",
                "department",
                "salary",
            ]
        ]
    )

    return ranked


# =============================================================================
# Department Distribution
# =============================================================================


def department_distribution(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Employee distribution across departments.
    """

    print_header("DEPARTMENT DISTRIBUTION")

    distribution = (
        df["department"]
        .value_counts()
        .rename_axis("department")
        .reset_index(name="employee_count")
    )

    print(distribution)

    return distribution


# =============================================================================
# Export Employee Reports
# =============================================================================


def export_employee_reports(
    employees: pd.DataFrame,
) -> None:
    """
    Export all employee reports.
    """

    logger.info("Exporting employee reports...")

    export_report(
        department_summary(employees),
        "department_summary.csv",
    )

    export_report(
        city_summary(employees),
        "city_summary.csv",
    )

    export_report(
        performance_summary(employees),
        "performance_summary.csv",
    )

    export_report(
        salary_ranking(employees),
        "salary_ranking.csv",
    )

    export_report(
        department_distribution(employees),
        "department_distribution.csv",
    )


# =============================================================================
# Employee Analytics Pipeline
# =============================================================================


def run_employee_analytics(
    datasets: Dict[str, pd.DataFrame],
) -> None:
    """
    Execute complete employee analytics workflow.
    """

    employees = datasets["employees"]

    employee_overview(employees)

    department_summary(employees)

    city_summary(employees)

    top_paid_employees(employees)

    performance_summary(employees)

    salary_ranking(employees)

    department_distribution(employees)

    export_employee_reports(employees) 
# =============================================================================
# Sales Analytics
# =============================================================================


def prepare_sales_data(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Prepare sales dataset.

    - Convert order_date to datetime
    - Calculate revenue
    """

    print_header("PREPARING SALES DATA")

    sales = sales.copy()

    sales["order_date"] = pd.to_datetime(
        sales["order_date"]
    )

    sales["revenue"] = (
        sales["quantity"]
        * (sales["price"] - sales["discount"])
    )

    print(sales.head())

    return sales


# =============================================================================
# Sales Overview
# =============================================================================


def sales_overview(
    sales: pd.DataFrame,
) -> None:
    """
    Display overall sales statistics.
    """

    print_header("SALES OVERVIEW")

    print(f"Total Orders      : {len(sales)}")
    print(f"Unique Customers  : {sales['customer_id'].nunique()}")
    print(f"Total Revenue     : {sales['revenue'].sum():,.2f}")
    print(f"Average Revenue   : {sales['revenue'].mean():,.2f}")
    print(f"Maximum Revenue   : {sales['revenue'].max():,.2f}")
    print(f"Minimum Revenue   : {sales['revenue'].min():,.2f}")


# =============================================================================
# Monthly Sales
# =============================================================================


def monthly_sales(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Monthly revenue report.
    """

    print_header("MONTHLY SALES")

    report = (
        sales.groupby(
            sales["order_date"].dt.to_period("M")
        )
        .agg(
            total_orders=("order_id", "count"),
            revenue=("revenue", "sum"),
        )
        .reset_index()
    )

    report["order_date"] = report["order_date"].astype(str)

    print(report)

    return report


# =============================================================================
# Category Analysis
# =============================================================================


def category_analysis(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Revenue by category.
    """

    print_header("CATEGORY ANALYSIS")

    report = (
        sales.groupby("category")
        .agg(
            total_quantity=("quantity", "sum"),
            total_revenue=("revenue", "sum"),
            average_price=("price", "mean"),
        )
        .round(2)
        .sort_values(
            by="total_revenue",
            ascending=False,
        )
        .reset_index()
    )

    print(report)

    return report


# =============================================================================
# Product Analysis
# =============================================================================


def product_analysis(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Product performance.
    """

    print_header("PRODUCT ANALYSIS")

    report = (
        sales.groupby("product")
        .agg(
            units_sold=("quantity", "sum"),
            revenue=("revenue", "sum"),
        )
        .sort_values(
            by="revenue",
            ascending=False,
        )
        .reset_index()
    )

    print(report)

    return report


# =============================================================================
# Salesperson Performance
# =============================================================================


def salesperson_performance(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Revenue generated by salesperson.
    """

    print_header("SALESPERSON PERFORMANCE")

    report = (
        sales.groupby("salesperson")
        .agg(
            orders=("order_id", "count"),
            revenue=("revenue", "sum"),
        )
        .sort_values(
            by="revenue",
            ascending=False,
        )
        .reset_index()
    )

    print(report)

    return report


# =============================================================================
# Top Revenue Orders
# =============================================================================


def top_orders(
    sales: pd.DataFrame,
    limit: int = 5,
) -> pd.DataFrame:
    """
    Highest revenue orders.
    """

    print_header("TOP REVENUE ORDERS")

    report = (
        sales.nlargest(
            limit,
            "revenue",
        )[
            [
                "order_id",
                "product",
                "customer_id",
                "salesperson",
                "revenue",
            ]
        ]
    )

    print(report)

    return report


# =============================================================================
# City Sales
# =============================================================================


def city_sales(
    sales: pd.DataFrame,
) -> pd.DataFrame:
    """
    Revenue by city.
    """

    print_header("CITY SALES")

    report = (
        sales.groupby("city")
        .agg(
            revenue=("revenue", "sum"),
            orders=("order_id", "count"),
        )
        .sort_values(
            by="revenue",
            ascending=False,
        )
        .reset_index()
    )

    print(report)

    return report


# =============================================================================
# Export Sales Reports
# =============================================================================


def export_sales_reports(
    sales: pd.DataFrame,
) -> None:
    """
    Export sales analytics reports.
    """

    logger.info("Exporting sales reports...")

    export_report(
        monthly_sales(sales),
        "monthly_sales.csv",
    )

    export_report(
        category_analysis(sales),
        "category_analysis.csv",
    )

    export_report(
        product_analysis(sales),
        "product_analysis.csv",
    )

    export_report(
        salesperson_performance(sales),
        "salesperson_performance.csv",
    )

    export_report(
        city_sales(sales),
        "city_sales.csv",
    )


# =============================================================================
# Sales Analytics Pipeline
# =============================================================================


def run_sales_analytics(
    datasets: Dict[str, pd.DataFrame],
) -> None:
    """
    Execute complete sales analytics workflow.
    """

    sales = prepare_sales_data(
        datasets["sales"]
    )

    sales_overview(sales)

    monthly_sales(sales)

    category_analysis(sales)

    product_analysis(sales)

    salesperson_performance(sales)

    top_orders(sales)

    city_sales(sales)

    export_sales_reports(sales)  