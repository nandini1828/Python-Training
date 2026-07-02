"""
Truthiness demonstration.
"""


def check(value):

    if value:
        print(f"{value!r} -> Truthy")

    else:
        print(f"{value!r} -> Falsy")


def demo():

    values = [
        [],
        {},
        "",
        (),
        set(),
        None,
        0,
        False,
        1,
        "Python",
        [1, 2],
        {"name": "Alice"},
    ]

    for item in values:
        check(item)