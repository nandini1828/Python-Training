from modules.loop_project.loops.for_loop import *


def test_print_numbers():
    assert print_numbers(5) == [1, 2, 3, 4, 5]


def test_even_numbers():
    assert even_numbers(10) == [2, 4, 6, 8, 10]


def test_square_numbers():
    assert square_numbers(4) == [1, 4, 9, 16]


def test_character_count():
    assert character_count("Indiana Jones") == 13


def test_find_max():
    assert find_max([10, 50, 20, 70, 30]) == 70


def test_table():
    table = multiplication_table(5)

    assert table[0] == "5 x 1 = 5"
    assert table[-1] == "5 x 10 = 50"


def test_dictionary():
    student = {
        "name": "Alice",
        "age": 22
    }

    assert dictionary_keys(student) == ["name", "age"]


def test_zip():
    names = ["Alice", "Bob"]
    scores = [90, 85]

    assert zip_names_scores(names, scores) == [
        ("Alice", 90),
        ("Bob", 85)
    ]


def test_enumerate():
    subjects = [
        "Python",
        "Django",
        "Pytest"
    ]

    assert enumerate_subjects(subjects) == [
        (1, "Python"),
        (2, "Django"),
        (3, "Pytest")
    ]