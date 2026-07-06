from .utils import *

def run_demo():
    print("=== any() and all() DEMO ===\n")

    nums = [0, 0, 5]

    print("1. any true:")
    print(check_any_true(nums))

    print("\n2. all true:")
    print(check_all_true(nums))

    print("\n3. any greater than 3:")
    print(any_greater_than(nums, 3))

    print("\n4. all greater than 0:")
    print(all_greater_than([1, 2, 3], 0))

    print("\n5. any even:")
    print(any_even([1, 3, 5, 6]))

    print("\n6. all even:")
    print(all_even([2, 4, 6]))

    print("\n7. any non-empty string:")
    print(any_non_empty(["", "", "hello"]))

    print("\n8. all non-empty string:")
    print(all_non_empty(["hi", "hello"]))

    print("\n9. any match condition:")
    print(any_match([1, 2, 3], lambda x: x > 2))

    print("\n10. all match condition:")
    print(all_match([2, 4, 6], lambda x: x % 2 == 0))


if __name__ == "__main__":
    run_demo()