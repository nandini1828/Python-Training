"""
Looking at Your Data
"""

import pandas as pd


def run():

    df = pd.read_csv("data/employees.csv")

    print("\n========== DATA INSPECTION ==========\n")

    print("Head")
    print(df.head())

    print("\nTail")
    print(df.tail())

    print("\nInfo")
    print(df.info())

    print("\nShape")
    print(df.shape)

    print("\nDescribe")
    print(df.describe())

    print("\nValue Counts")
    print(df["department"].value_counts())

    print("\nUnique Cities")
    print(df["city"].unique())