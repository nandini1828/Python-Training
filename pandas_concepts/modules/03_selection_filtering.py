"""
Selecting and Filtering Data
"""

import pandas as pd


def run():

    df = pd.read_csv("data/employees.csv")

    print("\n========== SELECTION ==========\n")

    print("Single Column")
    print(df["name"])

    print("\nMultiple Columns")
    print(df[["name", "salary"]])

    print("\nloc Example")
    print(df.loc[0, "name"])

    print("\niloc Example")
    print(df.iloc[0, 1])

    print("\nAge > 28")
    print(df[df["age"] > 28])

    print("\nAge > 28 AND City == Chicago")

    result = df[(df["age"] > 28) & (df["city"] == "Chicago")]

    print(result)