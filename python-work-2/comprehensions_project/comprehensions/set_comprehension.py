"""
Set Comprehension.
"""


def get_unique_lowercase(words):
    return {
        word.lower()
        for word in words
    }


def demo():
    words = [
        "Python",
        "JAVA",
        "python",
        "Java",
    ]

    unique = get_unique_lowercase(words)

    print(unique)


if __name__ == "__main__":
    demo()