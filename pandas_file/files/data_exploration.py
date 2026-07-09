import pandas as pd


def data_exploration():

    print("\n" + "=" * 70)
    print("              LOOKING AT YOUR DATA")
    print("=" * 70)

    try:

        df = pd.read_csv("data/insurance_policies.csv")

    except FileNotFoundError:

        print("\nInsurance policy file not found.")
        print("Please run Option 1 first.\n")
        return

    # --------------------------------------------------
    # 1. Head
    # --------------------------------------------------

    print("\n1. First Five Records (head())\n")

    print(df.head())

    # --------------------------------------------------
    # 2. Tail
    # --------------------------------------------------

    print("\n2. Last Five Records (tail())\n")

    print(df.tail())

    # --------------------------------------------------
    # 3. Info
    # --------------------------------------------------

    print("\n3. DataFrame Information (info())\n")

    df.info()

    # --------------------------------------------------
    # 4. Shape
    # --------------------------------------------------

    print("\n4. Shape of DataFrame\n")

    rows, columns = df.shape

    print(f"Rows    : {rows}")
    print(f"Columns : {columns}")

    # --------------------------------------------------
    # 5. Describe
    # --------------------------------------------------

    print("\n5. Statistical Summary (describe())\n")

    print(df.describe())

    # --------------------------------------------------
    # 6. Value Counts
    # --------------------------------------------------

    print("\n6. Policy Status Count\n")

    print(df["Status"].value_counts())

    # --------------------------------------------------
    # 7. Unique Values
    # --------------------------------------------------

    print("\n7. Unique Policy Types\n")

    print(df["Policy_Type"].unique())

    print("\nData Exploration Completed Successfully.")