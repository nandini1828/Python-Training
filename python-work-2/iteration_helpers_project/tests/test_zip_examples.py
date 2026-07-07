from iteration_helpers import zip_examples


def test_zip_demo_output(capsys):
    zip_examples.demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "Alice 90",
        "Bob 85",
        "Charlie 78",
        "",
        "('Alice', 'Delhi')",
        "('Bob', 'N/A')",
        "('Charlie', 'N/A')",
    ]
