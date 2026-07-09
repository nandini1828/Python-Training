from files import *


def display_menu():

    print("\n" + "=" * 70)
    print("         INSURANCE POLICY MANAGEMENT SYSTEM")
    print("=" * 70)

    print("1. Getting Started & Importing")
    print("2. Looking At Your Data")
    print("3. Selecting & Filtering Data")
    print("4. Cleaning & Editing Data")
    print("5. Grouping, Sorting & Combining")
    print("0. Exit")

    print("=" * 70)


def main():

    while True:

        display_menu()

        choice = input("Enter your choice : ")

        if choice == "1":
            getting_started()

        elif choice == "2":
            data_exploration()

        elif choice == "3":
            data_selection_filtering()

        elif choice == "4":
            data_cleaning_editing()

        elif choice == "5":
            grouping_sorting_combining()

        elif choice == "0":

            print("\nThank You...")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()