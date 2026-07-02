# Python Control Flow Mastery

This project demonstrates Python control flow concepts in a clean, modular structure.

## Topics Covered

### Conditionals
- if / elif / else
- Truthy and Falsy values
- Logical Operators
- Short-Circuit Evaluation
- Ternary Operator
- match-case

### Exercises
- Grade Calculator
- Login Validator
- Traffic Signal Decision Logic

### Testing
Pytest-based unit tests are included for all major conditional modules.

## Project Structure

```text
python_control_flow_mastery/
│
├── main.py
├── pytest.ini
├── README.md
│
├── conditionals/
│   ├── __init__.py
│   ├── if_else.py
│   ├── truthy_falsy.py
│   ├── logical_operators.py
│   ├── short_circuit.py
│   ├── ternary.py
│   └── match_case.py
│
├── exercises/
│   ├── __init__.py
│   ├── grade_calculator.py
│   ├── login_validator.py
│   └── traffic_signal.py
│
├── tests/
│   ├── test_if_else.py
│   ├── test_truthy.py
│   ├── test_logical.py
│   ├── test_ternary.py
│   └── test_match_case.py
│
└── docs/
    └── overview.md