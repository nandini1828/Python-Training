# 🐍 Python Control Flow

A beginner-friendly Python project that demonstrates the fundamentals of **Control Flow** using a **Smart ATM System**. Each topic is implemented with real-world examples to make learning practical and easy to understand.

---

## 📖 About the Project

Control flow is one of the most important concepts in programming. It determines how a program makes decisions and executes different blocks of code based on conditions.

This project explains Python's control flow concepts through a Smart ATM application instead of isolated examples.

Topics covered include:

- Conditional Statements (`if`, `elif`, `else`)
- Truthy and Falsy Values
- Logical Operators (`and`, `or`, `not`)
- Short-Circuit Evaluation
- Ternary Operator
- Structural Pattern Matching (`match-case`)

---

## 📂 Project Structure

```text
control_flow/
│
├── main.py
├── README.md
│
├── control_flow/
│   ├── __init__.py
│   ├── conditionals.py
│   ├── truthy_falsy.py
│   ├── logical_operators.py
│   ├── short_circuit.py
│   ├── ternary_operator.py
│   └── pattern_matching.py
│
└── tests/
    ├── __init__.py
    ├── test_conditionals.py
    ├── test_truthy_falsy.py
    ├── test_logical_operators.py
    ├── test_short_circuit.py
    ├── test_ternary_operator.py
    └── test_pattern_matching.py
```

---

# 🚀 Features

- Real-world Smart ATM examples
- Beginner-friendly code
- Well-commented source code
- Modular design
- Professional project structure
- Unit tests using `pytest`
- Easy to extend with new examples

---

# 📚 Topics Covered

## 1. Conditionals

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Decision making

Example:

- Card verification
- PIN verification
- Withdrawal
- Loan eligibility

---

## 2. Truthy & Falsy

Learn how Python evaluates:

- `None`
- `0`
- Empty string
- Empty list
- Empty dictionary
- Empty set

Example:

- Empty transaction history
- Missing ATM card
- Empty PIN

---

## 3. Logical Operators

Learn:

- `and`
- `or`
- `not`

Example:

- ATM login
- Premium customer access
- Loan approval
- Security alerts

---

## 4. Short-Circuit Evaluation

Understand how Python avoids unnecessary evaluations.

Examples include:

- Authentication
- Balance verification
- Customer support routing

---

## 5. Ternary Operator

Learn concise conditional expressions.

Example:

```python
status = "Approved" if balance >= amount else "Rejected"
```

---

## 6. Pattern Matching

Requires **Python 3.10+**

Topics:

- `match`
- `case`
- OR Pattern (`|`)
- Guard Conditions
- Default Case (`_`)

Example:

- ATM Menu
- Transaction Status
- Withdrawal Limits

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd control_flow
```

Run:

```bash
python main.py
```

---

# 🧪 Running Tests

Install pytest if needed:

```bash
pip install pytest
```

Run all tests:

```bash
pytest
```

Verbose output:

```bash
pytest -v
```

Run a single test:

```bash
pytest tests/test_conditionals.py
```

---

# 🎯 Learning Objectives

After completing this project, you will understand:

- How Python makes decisions
- How Boolean expressions work
- Truthy and falsy values
- Combining conditions
- Short-circuit evaluation
- Writing cleaner code using ternary operators
- Structural pattern matching
- Organizing Python projects
- Writing basic unit tests with `pytest`

---

# 💻 Requirements

- Python 3.10+
- pytest (for testing)

---

# 📌 Future Improvements

Possible enhancements include:

- User input instead of hardcoded values
- Database integration
- File handling for transaction history
- Object-Oriented ATM system
- Exception handling
- Logging
- REST API using FastAPI
- Web interface using Flask or Django

---

# 📖 References

- Python Official Documentation
- PEP 634 – Structural Pattern Matching
- Pytest Documentation

---

# 🤝 Contributing

Contributions are welcome!

Feel free to:

- Improve examples
- Fix bugs
- Add more test cases
- Enhance documentation

---

# 📄 License

This project is intended for educational purposes.