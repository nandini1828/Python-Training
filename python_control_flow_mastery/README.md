# Python Control Flow Mastery

This project is a beginner-friendly training repository that demonstrates Python control flow, loops, iteration, comprehensions, iterators, generators, and CLI design.

## Project structure

- conditionals/: conditional logic and branching examples
- loops/: for/while loops and flow-control keywords
- iteration/: range, enumerate, zip, reversed, sorted, any, all
- collections_iteration/: list, dictionary, set, and safe traversal patterns
- comprehensions/: list, dictionary, set, and nested comprehensions
- iterators_generators/: iterator protocol and generators
- cli/: argparse-based command-line examples
- tests/: pytest coverage for the training modules

## Concepts covered

- if/else and nested conditionals
- logical operators and short-circuit evaluation
- ternary operators and match-case
- for and while loops with break/continue/pass
- iteration helpers such as range, enumerate, zip, reversed, sorted
- comprehensions and generator expressions
- iterator protocol and custom iterators
- testing and CLI integration

## Run the application

```bash
python3 main.py --module all
```

## CLI usage

```bash
python3 main.py --module conditionals
python3 main.py --module loops
python3 main.py --module iteration
python3 main.py --module collections
python3 main.py --module comprehensions
python3 main.py --module generators
```

## Run tests

```bash
pytest
```

## Coverage report

```bash
pytest --cov=python_control_flow_mastery --cov-report=html
```
