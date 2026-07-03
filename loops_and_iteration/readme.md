# Python Loops & Iteration

A beginner-friendly Python project that demonstrates the fundamentals of **Loops and Iteration** using a **Smart Inventory Management System**. Each topic is implemented with real-world examples to make learning practical and easy to understand.

---

## About the Project

Loops are one of the most fundamental concepts in programming. They allow you to execute a block of code repeatedly, which is essential for processing collections of data and handling repetitive tasks efficiently.

This project explains Python's loop concepts through an inventory management application instead of isolated examples.

Topics covered include:

- **For Loops**: Iterating sequentially over collections, ranges, and string characters
- **While Loops**: Repeating a block of code based on a conditional state
- **Break Statement**: Exiting a loop prematurely
- **Continue Statement**: Skipping the current iteration and starting the next one
- **Pass Statement**: A null statement used as a placeholder in loops
- **For-Else Clause**: Code blocks that execute *only* if the loop completes without a `break`
- **While-Else Clause**: Code blocks that execute *only* if the loop completes without a `break`

---

## Project Structure

```text
loops_and_iteration/
│
├── main.py                      # Interactive menu entry point
├── README.md                    # Project documentation
├── __init__.py                  # Package initialization
│
├── for_loops.py                 # For loop demonstrations
├── while_loops.py               # While loop demonstrations
├── break_continue_pass.py       # Loop control statements
├── for_else_while_else.py       # Conditional loop completion
│
└── tests/
    ├── __init__.py
    ├── test_for_loops.py
    ├── test_while_loops.py
    ├── test_break_continue_pass.py
    └── test_for_else_while_else.py
```

---

## Topics Explained

### 1. For Loops (`for_loops.py`)

**What it is**: A loop that iterates over a sequence of items (list, tuple, string, dict, range, etc.)

**Key Features**:
- Iterate over lists, tuples, and other iterables
- Use `range()` for numeric iteration
- Use `enumerate()` to get both index and value
- Use `zip()` to iterate over multiple sequences in parallel
- Nested loops for multi-dimensional data processing

**Real-World Examples**:
- Processing product inventory lists
- Generating inventory reports with proper formatting
- Searching through warehouse sections
- Formatting and displaying data

**Code Highlights**:
```python
# Iterate over dictionary items
for product, details in inventory.items():
    print(f"{product}: {details['quantity']} units")

# Iterate with enumerate
for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")

# Nested loops for 2D data
for section, products in warehouse.items():
    for product in products:
        print(f"{section}: {product}")
```

---

### 2. While Loops (`while_loops.py`)

**What it is**: A loop that repeats as long as a condition is `True`

**Key Features**:
- Conditional repetition based on state
- No predetermined number of iterations
- Useful for event-driven and input-based loops
- Can loop indefinitely if condition never becomes `False`

**Real-World Examples**:
- User input validation with retry limits
- Stock depletion simulation
- Automated reorder systems
- ATM menu selection
- Authentication attempts with retry limits

**Code Highlights**:
```python
# Countdown timer
while count > 0:
    print(f"Alert in {count} seconds...")
    count -= 1

# Reorder system with multiple conditions
while day < max_days and stock > 0:
    sales = random.randint(5, 15)
    stock -= sales
    if stock < threshold:
        stock += reorder_amount
```

---

### 3. Break, Continue, Pass (`break_continue_pass.py`)

**Break Statement**: Exits a loop immediately

**When to use**:
- Found the item you're searching for
- Condition met, no need to continue
- Prevent unnecessary iterations

**Example**:
```python
for item in items:
    if item == target:
        print(f"Found: {item}")
        break
```

---

**Continue Statement**: Skips current iteration, goes to next one

**When to use**:
- Skip invalid or unwanted items
- Filter data during iteration
- Avoid nested if statements

**Example**:
```python
for product in products:
    if product['stock'] == 0:
        continue  # Skip out-of-stock items
    print(product['name'])
```

---

**Pass Statement**: A null statement (does nothing)

**When to use**:
- Placeholder for future code
- Required by Python syntax but no action needed
- Skeleton code development

**Example**:
```python
for product in products:
    # Future: Validate product
    pass
    
    # Future: Update database
    pass
```

---

### 4. For-Else & While-Else (`for_else_while_else.py`)

**For-Else**: The `else` block executes if the loop completes **without** encountering a `break`

**Key Point**: The `else` clause does NOT execute if you `break` out of the loop

**When to use**:
- Confirm search operations
- Validate that all items met criteria
- Execute cleanup code after normal loop completion

**Example**:
```python
for product in inventory:
    if product == search_item:
        print("Found!")
        break
else:
    print("Item not found!")  # Only prints if loop completes without break
```

---

**While-Else**: Same concept as for-else but with while loops

**Example**:
```python
while attempts < max_attempts:
    if validate_input():
        break
    attempts += 1
else:
    print("Max attempts exceeded!")  # Only if loop completes without break
```

---

## Real-World Context: Inventory Management System

All examples are implemented within the context of a **Smart Inventory Management System**:

- **Products**: Laptop, Mouse, Keyboard, Monitor, Headphones
- **Operations**: Stock checking, reordering, transaction processing
- **Scenarios**: Out-of-stock detection, budget verification, warehouse organization

This context makes the concepts practical and relatable to real-world programming scenarios.

---

## Running the Project

### Interactive Menu (Recommended)
```bash
python main.py
```

This opens an interactive menu where you can:
1. Explore For Loops
2. Explore While Loops
3. Explore Break, Continue, Pass
4. Explore For-Else & While-Else
5. Run all examples
6. Exit

### Individual Modules
```bash
python for_loops.py
python while_loops.py
python break_continue_pass.py
python for_else_while_else.py
```

---

## Running Tests

```bash
pytest tests/
```

Or run specific test files:
```bash
pytest tests/test_for_loops.py
pytest tests/test_while_loops.py
pytest tests/test_break_continue_pass.py
pytest tests/test_for_else_while_else.py
```

---

## Key Concepts Summary

| Concept | Purpose | When to Use |
|---------|---------|------------|
| **For Loop** | Iterate over collections | Known number of items or sequences |
| **While Loop** | Repeat based on condition | Dynamic iteration, input handling |
| **Break** | Exit loop immediately | Found target, condition met |
| **Continue** | Skip to next iteration | Filter unwanted items |
| **Pass** | Null statement | Placeholder for future code |
| **For-Else** | Run if loop completes normally | Search confirmation, validation |
| **While-Else** | Run if loop completes normally | Exhaustive checking, validation |

---

## Learning Flow

1. **Start with For Loops** - Understand basic iteration
2. **Move to While Loops** - Learn conditional repetition
3. **Master Loop Control** - Use break, continue, pass effectively
4. **Advanced Patterns** - Combine with else clauses for robust code

---

## Tips for Learning

1. **Experiment**: Run the interactive menu and try different scenarios
2. **Modify Examples**: Change values and see how behavior changes
3. **Trace Execution**: Follow the output to understand loop flow
4. **Real-World Context**: Connect concepts to inventory operations
5. **Combine Concepts**: Mix multiple loop types in your own code

---

## Common Pitfalls to Avoid

1. **Infinite Loops**: Ensure while loop condition eventually becomes `False`
2. **Off-by-One Errors**: Be careful with range boundaries
3. **Break Scope**: Remember break only exits current loop, not nested loops
4. **Else Clause Confusion**: else runs only if loop completes without break
5. **Continue in While**: Ensure loop condition changes, or you'll loop forever

---

## Next Steps

After mastering loops, explore:
- List comprehensions (compact loops)
- Generators and iterators
- Iterator protocol
- Functional programming tools (map, filter)

---

## Author's Notes

This project emphasizes:
- **Practical Learning**: Real-world scenarios over abstract examples
- **Clear Output**: Formatted output to understand loop behavior
- **Incremental Complexity**: Simple examples building to complex patterns
- **Common Mistakes**: Highlighting and avoiding typical errors

Happy Learning! 🚀
