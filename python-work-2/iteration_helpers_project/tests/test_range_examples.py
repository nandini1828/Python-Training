from iteration_helpers import range_examples


def test_range_demo_output(capsys):
    range_examples.demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "[0, 1, 2, 3, 4]",
        "[2, 3, 4, 5, 6, 7, 8, 9]",
        "[1, 4, 7, 10, 13, 16, 19]",
    ]
