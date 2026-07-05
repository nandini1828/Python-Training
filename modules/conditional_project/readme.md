# Conditional Control Flow Project

## Objective

This project demonstrates Python's conditional control flow concepts using
modular programming.

Topics Covered

- if-elif-else
- Truthy and Falsy
- Logical Operators
- Short Circuit Evaluation
- Ternary Operator
- Match Case (Python 3.10+)

Project Structure

```
conditional_project/
│
├── main.py
├── pytest.ini
├── requirements.txt
├── README.md
│
├── conditions/
│   ├── if_else.py
│   ├── logical.py
│   ├── truthy.py
│   ├── short_circuit.py
│   ├── ternary.py
│   └── match_case.py
│
└── tests/
```

Run the project

```
python main.py
```

Run all tests

```
pytest
```

Coverage

```
pytest --cov=conditions --cov-report=html
```

Open

```
htmlcov/index.html
```

to view the report.