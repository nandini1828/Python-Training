from .utils import *

def run_demo():
    print("=== ENUMERATE MODULE DEMO ===\n")

    data = ["a", "b", "c", "a"]

    print("1. Basic enumerate:")
    print(index_items(data))

    print("\n2. Custom start:")
    print(index_with_start(data, start=10))

    print("\n3. Find positions of 'a':")
    print(find_item_positions(data, "a"))

    print("\n4. Index mapping:")
    print(create_index_mapping(data))

    print("\n5. Even index elements:")
    print(filter_with_index(data))

    print("\n6. Enumerate string:")
    print(enumerate_string("hello"))

    print("\n7. Compare lists:")
    print(compare_lists([1,2,3], [1,5,3]))


if __name__ == "__main__":
    run_demo()