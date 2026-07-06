from python_control_flow_mastery.cli.argparse_demo import build_parser, run_demo


def test_build_parser_defaults_to_all_module(capsys):
    parser = build_parser()
    args = parser.parse_args([])
    assert args.module == "all"
    run_demo(args.module)
    captured = capsys.readouterr()
    assert "Conditionals demo:" in captured.out


def test_run_demo_for_conditionals(capsys):
    run_demo("conditionals")
    captured = capsys.readouterr()
    assert "ATM menu" in captured.out
