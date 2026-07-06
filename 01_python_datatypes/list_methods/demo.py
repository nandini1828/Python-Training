"""Demo Program for List Methods"""

from list_methods.list_utils import unique, chunk


def main() -> None:
    items = [1, 2, 1, 3, 4]
    print("Unique:", unique(items))
    print("Chunks:", chunk(items, 2))


if __name__ == "__main__":
    main()