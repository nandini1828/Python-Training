from comprehensions.set_comprehensions import set_comprehension_example


def test_set_comprehension_creates_unique_lowercase_values():
    values = ["Laptop", "Mouse", "Laptop", "Keyboard", "mouse"]
    assert set_comprehension_example(values) == {"laptop", "mouse", "keyboard"}
