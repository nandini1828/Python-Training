"""
Set Comprehension.
"""


def demo():

    words = [
        "Python",
        "JAVA",
        "python",
        "Java"
    ]

    unique = {
        word.lower()
        for word in words
    }

    print(unique)