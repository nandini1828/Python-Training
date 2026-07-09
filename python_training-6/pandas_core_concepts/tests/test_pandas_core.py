"""
test_pandas_core.py

Pytest test cases for Pandas Core Concepts.
"""

from model import PandasData


def test_dataframe_creation():
    """Test if employees DataFrame is created correctly."""
    df = PandasData.employees()

    assert not df.empty
    assert df.shape == (5, 6)


def test_column_names():
    """Test expected column names."""
    df = PandasData.employees()

    expected_columns = [
        "ID",
        "Name",
        "Age",
        "Department",
        "Salary",
        "City"
    ]

    assert list(df.columns) == expected_columns


def test_head():
    """Test head()."""
    df = PandasData.employees()

    assert len(df.head(3)) == 3


def test_tail():
    """Test tail()."""
    df = PandasData.employees()

    assert len(df.tail(2)) == 2


def test_shape():
    """Test shape."""
    df = PandasData.employees()

    assert df.shape[0] == 5
    assert df.shape[1] == 6


def test_select_column():
    """Test selecting a column."""
    df = PandasData.employees()

    assert "Name" in df.columns


def test_filter_salary():
    """Test filtering employees by salary."""
    df = PandasData.employees()

    filtered = df[df["Salary"] > 50000]

    assert len(filtered) == 3


def test_unique_departments():
    """Test unique departments."""
    df = PandasData.employees()

    departments = df["Department"].unique()

    assert len(departments) == 3


def test_value_counts():
    """Test value_counts()."""
    df = PandasData.employees()

    counts = df["Department"].value_counts()

    assert counts["HR"] == 2
    assert counts["IT"] == 2
    assert counts["Finance"] == 1


def test_sort_values():
    """Test sorting by salary."""
    df = PandasData.employees()

    sorted_df = df.sort_values(by="Salary")

    assert sorted_df.iloc[0]["Salary"] == 40000


def test_groupby_mean():
    """Test groupby()."""
    df = PandasData.employees()

    result = df.groupby("Department")["Salary"].mean()

    assert result["HR"] == 42500


def test_add_column():
    """Test adding a new column."""
    df = PandasData.employees()

    df["Bonus"] = df["Salary"] * 0.10

    assert "Bonus" in df.columns


def test_rename_column():
    """Test renaming a column."""
    df = PandasData.employees()

    renamed = df.rename(columns={"Salary": "Monthly_Salary"})

    assert "Monthly_Salary" in renamed.columns


def test_drop_column():
    """Test dropping a column."""
    df = PandasData.employees()

    dropped = df.drop(columns=["City"])

    assert "City" not in dropped.columns


def test_drop_duplicates():
    """Test drop_duplicates()."""
    df = PandasData.employees()

    unique_df = df.drop_duplicates()

    assert len(unique_df) == len(df)