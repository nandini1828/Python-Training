"""
Utility functions for displaying formatted output.
"""


def print_heading(title):
    """Print a formatted heading."""

    print("\n" + "=" * 70)
    print(title.upper())
    print("=" * 70)


def print_subheading(title):
    """Print a formatted subheading."""

    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)


def separator():
    """Print a separator line."""

    print("-" * 60)


def show_dataframe(df, rows=5):
    """
    Display the first few rows of a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to display.
    rows : int
        Number of rows to display.
    """

    print(df.head(rows))


def print_shape(df):
    """Display DataFrame shape."""

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")


def print_columns(df):
    """Display DataFrame columns."""

    print("Columns:")
    for column in df.columns:
        print(f"• {column}")


def print_message(message):
    """Print a formatted message."""

    print(f"\n>>> {message}")