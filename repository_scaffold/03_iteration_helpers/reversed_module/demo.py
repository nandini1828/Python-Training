from .utils import *

def run_demo():
    print("=== reversed() DEMO ===\n")

    print("1. Reverse list:")
    print(reverse_list([1, 2, 3, 4]))

    print("\n2. Reverse string:")
    print(reverse_string("ganesh"))

    print("\n3. Reverse tuple:")
    print(reverse_tuple((10, 20, 30)))

    print("\n4. Reverse range:")
    print(reverse_range(1, 6))

    print("\n5. Reverse words:")
    print(reverse_words("I love Python"))

    print("\n6. Reverse each word:")
    print(reverse_each_word("hello world"))

    print("\n7. Palindrome check:")
    print(is_palindrome("madam"))

    print("\n8. Reverse using slicing:")
    print(reverse_with_slice([5, 6, 7]))


if __name__ == "__main__":
    run_demo()