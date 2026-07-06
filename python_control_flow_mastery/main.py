"""Interactive entry point for the control flow mastery project."""

from __future__ import annotations

try:
    from .cli.argparse_demo import build_parser, run_demo
except ImportError:  # pragma: no cover - supports direct script execution
    from cli.argparse_demo import build_parser, run_demo


def main() -> None:
    """Parse CLI arguments and run the requested demonstration."""
    parser = build_parser()
    args = parser.parse_args()
    run_demo(args.module)


if __name__ == "__main__":
    main()
