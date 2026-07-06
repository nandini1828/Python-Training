from .utils import *

def run_demo():
    print("=== ZIP MODULE DEMO ===\n")

    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    list3 = [True, False, True]

    print("1. Pair lists:")
    print(pair_lists(list1, list2))

    print("\n2. Multiple lists:")
    print(pair_multiple_lists(list1, list2, list3))

    print("\n3. Zip with index:")
    print(zip_with_index(list2))

    print("\n4. Uneven zip:")
    print(uneven_zip([1, 2], ["a", "b", "c"], fill_value="X"))

    print("\n5. Unzip pairs:")
    pairs = [(1, "a"), (2, "b")]
    print(list(unzip_pairs(pairs)))

    print("\n6. Create dict:")
    print(create_dict(["id", "name"], [1, "Ganesh"]))

    print("\n7. Compare lists:")
    print(compare_lists([1, 2, 3], [1, 5, 3]))

    print("\n8. Sum pairs:")
    print(sum_pairs([1, 2, 3], [4, 5, 6]))

    print("\n9. Transpose matrix:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose_matrix(matrix))


if __name__ == "__main__":
    run_demo()