from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_sales_data() -> pd.DataFrame:
    sales_file = DATASET_DIR / "sales.csv"
    return pd.read_csv(sales_file)


def add_revenue_column(df: pd.DataFrame) -> pd.DataFrame:
    updated_df = df.copy()
    updated_df["revenue"] = updated_df["quantity"] * updated_df["price"]
    return updated_df


def pivot_average_price_by_category_city(df: pd.DataFrame):
    print("\n--- Pivot: Average Price by Category and City ---")
    pivot_df = pd.pivot_table(
        df,
        values="price",
        index="category",
        columns="city",
        aggfunc="mean"
    )
    print(pivot_df)


def pivot_total_revenue_by_category_city(df: pd.DataFrame):
    print("\n--- Pivot: Total Revenue by Category and City ---")
    revenue_df = add_revenue_column(df)

    pivot_df = pd.pivot_table(
        revenue_df,
        values="revenue",
        index="category",
        columns="city",
        aggfunc="sum",
        fill_value=0
    )
    print(pivot_df)


def main():
    print("Pandas - Pivot Table Intro")
    sales_df = load_sales_data()

    pivot_average_price_by_category_city(sales_df)
    pivot_total_revenue_by_category_city(sales_df)


if __name__ == "__main__":
    main()