import pandas as pd


def data_cleaning_editing():

    print("\n" + "=" * 70)
    print("             CLEANING & EDITING DATA")
    print("=" * 70)

    try:

        df = pd.read_csv("data/insurance_policies.csv")

    except FileNotFoundError:

        print("\nInsurance policy file not found.")
        print("Please run Option 1 first.\n")
        return

    # --------------------------------------------------
    # Create Sample Missing Values
    # --------------------------------------------------

    print("\n1. Creating Sample Missing Values\n")

    df.loc[1, "Premium"] = None
    df.loc[3, "City"] = None

    print(df)

    # --------------------------------------------------
    # Find Null Values
    # --------------------------------------------------

    print("\n2. Finding Null Values\n")

    print(df.isnull().sum())

    # --------------------------------------------------
    # Fill Missing Premium
    # --------------------------------------------------

    print("\n3. Filling Missing Premium with 20000\n")

    df["Premium"] = df["Premium"].fillna(20000)

    # --------------------------------------------------
    # Fill Missing City
    # --------------------------------------------------

    print("\n4. Filling Missing City with 'Unknown'\n")

    df["City"] = df["City"].fillna("Unknown")

    print(df)

    # --------------------------------------------------
    # Add New Column
    # --------------------------------------------------

    print("\n5. Adding GST (18%)\n")

    df["GST"] = df["Premium"] * 0.18

    print(df)

    # --------------------------------------------------
    # Add Total Premium Column
    # --------------------------------------------------

    print("\n6. Adding Total Premium\n")

    df["Total_Premium"] = df["Premium"] + df["GST"]

    print(df)

    # --------------------------------------------------
    # Change Data Type
    # --------------------------------------------------

    print("\n7. Changing Premium to Integer\n")

    df["Premium"] = df["Premium"].astype(int)

    print(df.dtypes)

    # --------------------------------------------------
    # Rename Columns
    # --------------------------------------------------

    print("\n8. Renaming Customer_Name to Customer\n")

    df.rename(
        columns={
            "Customer_Name": "Customer"
        },
        inplace=True
    )

    print(df.columns)

    # --------------------------------------------------
    # Drop Column
    # --------------------------------------------------

    print("\n9. Dropping GST Column\n")

    df.drop(columns=["GST"], inplace=True)

    print(df)

    # --------------------------------------------------
    # Create Duplicate Row
    # --------------------------------------------------

    print("\n10. Creating Duplicate Record\n")

    duplicate = pd.concat([df, df.iloc[[0]]], ignore_index=True)

    print(duplicate)

    # --------------------------------------------------
    # Remove Duplicate
    # --------------------------------------------------

    print("\n11. Removing Duplicate Records\n")

    duplicate = duplicate.drop_duplicates()

    print(duplicate)

    # --------------------------------------------------
    # Drop Rows with Null Values
    # --------------------------------------------------

    print("\n12. Dropping Rows with Null Values\n")

    clean_df = duplicate.dropna()

    print(clean_df)

    # --------------------------------------------------
    # Save Cleaned Data
    # --------------------------------------------------

    clean_df.to_csv(
        "data/cleaned_insurance_policies.csv",
        index=False
    )

    print("\nCleaned data saved successfully.")

    print("\nCleaning & Editing Completed Successfully.")