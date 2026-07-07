from iteration_helpers import reversed_sorted


def test_reversed_sorted_demo_output(capsys):
    reversed_sorted.demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "[2, 7, 1, 5]",
        "Bob 70",
        "Charlie 80",
        "Alice 90",
    ]
