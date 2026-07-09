import pandas as pd


def data_selection_filtering():

    print("\n" + "=" * 70)
    print("           SELECTING & FILTERING DATA")
    print("=" * 70)

    try:

        df = pd.read_csv("data/insurance_policies.csv")

    except FileNotFoundError:

        print("\nInsurance policy file not found.")
        print("Please run Option 1 first.\n")
        return

    # --------------------------------------------------
    # 1. Select Single Column
    # --------------------------------------------------

    print("\n1. Selecting Customer_Name Column\n")

    print(df["Customer_Name"])

    # --------------------------------------------------
    # 2. Select Multiple Columns
    # --------------------------------------------------

    print("\n2. Selecting Multiple Columns\n")

    print(df[["Customer_Name", "Policy_Type", "Premium"]])

    # --------------------------------------------------
    # 3. Using loc[]
    # --------------------------------------------------

    print("\n3. Selecting Row using loc[]\n")

    print(df.loc[2])

    # --------------------------------------------------
    # 4. Using iloc[]
    # --------------------------------------------------

    print("\n4. Selecting Row using iloc[]\n")

    print(df.iloc[1])

    # --------------------------------------------------
    # 5. Selecting Specific Rows and Columns
    # --------------------------------------------------

    print("\n5. Selecting Rows 1 to 3 and Columns 1 to 4\n")

    print(df.iloc[1:4, 1:5])

    # --------------------------------------------------
    # 6. Filter Premium > 20000
    # --------------------------------------------------

    print("\n6. Policies having Premium greater than 20000\n")

    premium_filter = df[df["Premium"] > 20000]

    print(premium_filter)

    # --------------------------------------------------
    # 7. Multiple Filters
    # --------------------------------------------------

    print("\n7. Active Policies in Hyderabad\n")

    multiple_filter = df[
        (df["Status"] == "Active") &
        (df["City"] == "Hyderabad")
    ]

    print(multiple_filter)

    # --------------------------------------------------
    # 8. Search Policy by ID
    # --------------------------------------------------

    print("\n8. Search Policy by Policy ID\n")

    policy_id = int(input("Enter Policy ID : "))

    result = df[df["Policy_ID"] == policy_id]

    if result.empty:

        print("\nPolicy Not Found")

    else:

        print("\nPolicy Details\n")

        print(result)

    # --------------------------------------------------
    # 9. Search Customer by Name
    # --------------------------------------------------

    print("\n9. Search Customer by Name\n")

    customer = input("Enter Customer Name : ").title()

    result = df[df["Customer_Name"] == customer]

    if result.empty:

        print("\nCustomer Not Found")

    else:

        print("\nCustomer Details\n")

        print(result)

    print("\nSelection & Filtering Completed Successfully.")