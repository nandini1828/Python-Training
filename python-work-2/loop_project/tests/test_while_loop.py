from loops import while_loop


def test_countdown_output(capsys):
    while_loop.countdown()
    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["5", "4", "3", "2", "1"]