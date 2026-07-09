"""
02_inspecting_data.py

Topics Covered:
1. head()
2. tail()
3. info()
4. shape
5. describe()
6. value_counts()
7. unique()
"""

from model import PandasData


def head_tail_demo():
    print("\n========== head() & tail() ==========")

    df = PandasData.employees()

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nFirst 3 Rows:")
    print(df.head(3))

    print("\nLast 5 Rows:")
    print(df.tail())

    print("\nLast 2 Rows:")
    print(df.tail(2))


def info_demo():
    print("\n========== info() ==========")

    df = PandasData.employees()
    df.info()


def shape_demo():
    print("\n========== shape ==========")

    df = PandasData.employees()

    print("Shape :", df.shape)
    print("Rows  :", df.shape[0])
    print("Columns :", df.shape[1])


def describe_demo():
    print("\n========== describe() ==========")

    df = PandasData.employees()

    print(df.describe())


def value_counts_demo():
    print("\n========== value_counts() ==========")

    df = PandasData.employees()

    print(df["Department"].value_counts())


def unique_demo():
    print("\n========== unique() ==========")

    df = PandasData.employees()

    print(df["City"].unique())


def run():
    head_tail_demo()
    info_demo()
    shape_demo()
    describe_demo()
    value_counts_demo()
    unique_demo()


if __name__ == "__main__":
    run()