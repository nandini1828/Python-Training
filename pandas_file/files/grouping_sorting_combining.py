import pandas as pd


def grouping_sorting_combining():

    print("\n" + "=" * 70)
    print("        GROUPING, SORTING & COMBINING DATA")
    print("=" * 70)

    try:

        policies = pd.read_csv("data/insurance_policies.csv")

    except FileNotFoundError:

        print("\nInsurance policy file not found.")
        print("Please run Option 1 first.\n")
        return

    # ---------------------------------------------------------
    # 1. Sort Policies by Premium
    # ---------------------------------------------------------

    print("\n1. Policies Sorted by Premium (Highest to Lowest)\n")

    sorted_df = policies.sort_values(
        by="Premium",
        ascending=False
    )

    print(sorted_df)

    # ---------------------------------------------------------
    # 2. Group Policies by Policy Type
    # ---------------------------------------------------------

    print("\n2. Average Premium by Policy Type\n")

    grouped = policies.groupby(
        "Policy_Type"
    )["Premium"].mean()

    print(grouped)

    # ---------------------------------------------------------
    # 3. Create Claims DataFrame
    # ---------------------------------------------------------

    print("\n3. Creating Claims Data\n")

    claims = pd.DataFrame({

        "Policy_ID": [
            101,
            102,
            103,
            105
        ],

        "Claim_Amount": [
            50000,
            120000,
            35000,
            70000
        ],

        "Claim_Status": [
            "Approved",
            "Pending",
            "Rejected",
            "Approved"
        ]

    })

    print(claims)

    # Save claims data

    claims.to_csv(
        "data/claims.csv",
        index=False
    )

    # ---------------------------------------------------------
    # 4. Merge Policies with Claims
    # ---------------------------------------------------------

    print("\n4. Merging Policies with Claims\n")

    merged_df = pd.merge(

        policies,

        claims,

        on="Policy_ID",

        how="left"

    )

    print(merged_df)

    # ---------------------------------------------------------
    # 5. Create New Policies
    # ---------------------------------------------------------

    print("\n5. Creating New Policy Records\n")

    new_policies = pd.DataFrame({

        "Policy_ID": [
            106,
            107
        ],

        "Customer_Name": [
            "Arjun",
            "Meena"
        ],

        "Age": [
            40,
            32
        ],

        "City": [
            "Delhi",
            "Pune"
        ],

        "Policy_Type": [
            "Health",
            "Life"
        ],

        "Premium": [
            42000,
            28000
        ],

        "Status": [
            "Active",
            "Pending"
        ]

    })

    print(new_policies)

    # ---------------------------------------------------------
    # 6. Concatenate DataFrames
    # ---------------------------------------------------------

    print("\n6. Concatenating Existing Policies with New Policies\n")

    all_policies = pd.concat(

        [policies, new_policies],

        ignore_index=True

    )

    print(all_policies)

    # ---------------------------------------------------------
    # 7. Save Updated Policies
    # ---------------------------------------------------------

    all_policies.to_csv(

        "data/all_policies.csv",

        index=False

    )

    print("\nUpdated policy data saved successfully.")

    print("\nGrouping, Sorting & Combining Completed Successfully.")