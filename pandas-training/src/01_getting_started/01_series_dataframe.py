import pandas as pd


def create_series_examples():
    print("\n--- Series Examples ---")

    marks_series = pd.Series([85, 90, 78, 92], name="marks")
    print("\nMarks Series:")
    print(marks_series)

    custom_index_series = pd.Series(
        [65000, 52000, 48000],
        index=["Karthik", "Rahul", "Ananya"],
        name="salary"
    )
    print("\nSalary Series with custom index:")
    print(custom_index_series)


def create_dataframe_examples():
    print("\n--- DataFrame Examples ---")

    employee_data = {
        "name": ["Karthik", "Rahul", "Ananya", "Sneha"],
        "department": ["Engineering", "Sales", "HR", "Engineering"],
        "salary": [65000, 52000, 48000, 61000],
        "city": ["Hyderabad", "Chennai", "Bangalore", "Hyderabad"]
    }

    employees_df = pd.DataFrame(employee_data)

    print("\nEmployee DataFrame:")
    print(employees_df)

    print("\nDataFrame columns:")
    print(employees_df.columns.tolist())

    print("\nDataFrame index:")
    print(employees_df.index.tolist())


def main():
    print("Pandas Getting Started - Series and DataFrame")
    create_series_examples()
    create_dataframe_examples()


if __name__ == "__main__":
    main()