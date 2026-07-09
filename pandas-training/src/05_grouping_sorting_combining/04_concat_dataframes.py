import pandas as pd


def create_sales_q1_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id": [1, 2, 3],
        "product": ["Laptop", "Mouse", "Monitor"],
        "amount": [55000, 1200, 15000]
    })


def create_sales_q2_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id": [4, 5, 6],
        "product": ["Keyboard", "Printer", "Desk"],
        "amount": [2000, 18000, 7000]
    })


def create_customer_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "customer_name": ["Aarav", "Diya", "Ishaan"]
    })


def row_wise_concat(df1: pd.DataFrame, df2: pd.DataFrame):
    print("\n--- Row-wise Concat (axis=0) ---")
    combined_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    print(combined_df)


def column_wise_concat(df1: pd.DataFrame, df2: pd.DataFrame):
    print("\n--- Column-wise Concat (axis=1) ---")
    combined_df = pd.concat([df1, df2], axis=1)
    print(combined_df)


def main():
    print("Pandas - Concat DataFrames")

    sales_q1_df = create_sales_q1_dataframe()
    sales_q2_df = create_sales_q2_dataframe()
    customer_df = create_customer_dataframe()

    print("\nSales Q1 DataFrame:")
    print(sales_q1_df)

    print("\nSales Q2 DataFrame:")
    print(sales_q2_df)

    row_wise_concat(sales_q1_df, sales_q2_df)
    column_wise_concat(sales_q1_df, customer_df)


if __name__ == "__main__":
    main()