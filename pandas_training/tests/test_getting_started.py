"""
Tests for getting_started package.
"""

import pandas as pd

from getting_started.series import (
    create_series_from_list,
    create_series_from_dictionary,
    create_series_with_custom_index,
)

from getting_started.dataframe import (
    create_dataframe_from_dictionary,
    create_dataframe_from_list,
)

from getting_started.csv_operations import read_csv_file


def test_read_csv():
    df = read_csv_file("employees.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10


def test_series_creation():
    series = pd.Series([10, 20, 30])

    assert len(series) == 3
    assert series.iloc[0] == 10


def test_series_dictionary():
    data = {
        "Math": 90,
        "Science": 80,
    }

    series = pd.Series(data)

    assert "Math" in series.index
    assert series["Math"] == 90


def test_custom_index():
    s = pd.Series(
        ["Apple", "Banana"],
        index=["A", "B"],
    )

    assert s.index.tolist() == ["A", "B"]


def test_dataframe_creation():
    df = pd.DataFrame(
        {
            "Name": ["A", "B"],
            "Age": [20, 21],
        }
    )

    assert df.shape == (2, 2)