import pandas as pd


class PandasBasics:
    """
    A collection of basic Pandas operations.

    This class demonstrates how to:
    - Create a Series
    - Create a DataFrame
    - Read data from a CSV file
    - Save a DataFrame to a CSV file
    """

    @staticmethod
    def create_series():
        """Create and return a Pandas Series."""

        return pd.Series(
            [10, 20, 30, 40, 50],
            name="Numbers"
        )

    @staticmethod
    def create_dataframe():
        """Create and return a simple DataFrame."""

        data = {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 30, 35],
            "City": ["New York", "Los Angeles", "Chicago"]
        }

        return pd.DataFrame(data)

    @staticmethod
    def load_csv(file_path):
        """Read a CSV file."""

        return pd.read_csv(file_path)

    @staticmethod
    def save_csv(df, output_file):
        """Save a DataFrame to a CSV file."""

        df.to_csv(output_file, index=False)

        print(f"Data saved successfully to '{output_file}'.")