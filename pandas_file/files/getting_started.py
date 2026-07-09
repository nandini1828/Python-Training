import os
import pandas as pd


def getting_started():

    print("\n" + "=" * 70)
    print("            GETTING STARTED & IMPORTING")
    print("=" * 70)

    # -------------------------------
    # Create Data Folder
    # -------------------------------

    if not os.path.exists("data"):
        os.makedirs("data")

    # -------------------------------
    # Create a Series
    # -------------------------------

    print("\n1. Creating a Pandas Series\n")

    premium_series = pd.Series(
        [15000, 22000, 18500, 30000, 27500],
        name="Annual Premium"
    )

    print(premium_series)

    # -------------------------------
    # Create DataFrame
    # -------------------------------

    print("\n2. Creating Insurance Policy DataFrame\n")

    policies = {

        "Policy_ID": [101, 102, 103, 104, 105],

        "Customer_Name": [
            "Rahul",
            "Priya",
            "Amit",
            "Sneha",
            "Kiran"
        ],

        "Age": [
            30,
            27,
            42,
            35,
            29
        ],

        "City": [
            "Hyderabad",
            "Bangalore",
            "Chennai",
            "Hyderabad",
            "Mumbai"
        ],

        "Policy_Type": [
            "Health",
            "Life",
            "Auto",
            "Home",
            "Travel"
        ],

        "Premium": [
            15000,
            22000,
            18500,
            30000,
            27500
        ],

        "Status": [
            "Active",
            "Active",
            "Expired",
            "Pending",
            "Active"
        ]

    }

    df = pd.DataFrame(policies)

    print(df)

    # -------------------------------
    # Save CSV
    # -------------------------------

    csv_path = "data/insurance_policies.csv"

    df.to_csv(csv_path, index=False)

    print("\nInsurance policies saved successfully.")

    # -------------------------------
    # Read CSV
    # -------------------------------

    print("\n3. Reading CSV File\n")

    policy_df = pd.read_csv(csv_path)

    print(policy_df)

    print("\nGetting Started Module Completed Successfully.")