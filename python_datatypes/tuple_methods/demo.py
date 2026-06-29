"""Demo Program for Tuple Methods"""

from tuple_methods.tuple_utils import to_list, count_value


def main() -> None:
    t = (1, 2, 2, 3)
    print("To list:", to_list(t))
    print("Count 2:", count_value(t, 2))


if __name__ == "__main__":
    main()