from loops import break_continue_pass


def test_break_demo_output(capsys):
    break_continue_pass.break_demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["0", "1", "2", "3", "4"]


def test_continue_demo_output(capsys):
    break_continue_pass.continue_demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["1", "3", "5", "7", "9"]


def test_pass_demo_output(capsys):
    break_continue_pass.pass_demo()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["Loop finished"]