# Breakpoint Debugging

## What is Debugging?

Debugging is the process of finding and fixing errors (bugs) in a program.

Instead of adding multiple print() statements, Python provides a debugger that allows us to pause the program and inspect everything happening at that moment.

A breakpoint is a point where the program temporarily stops execution so that the programmer can inspect variables, understand the execution flow, and identify issues.

Python provides a built-in function:

```python
breakpoint()
```

When execution reaches this line, the debugger starts.

Modern IDEs like VS Code and PyCharm also allow graphical breakpoints without writing breakpoint() in the code.

---

## Why use Breakpoints?

Breakpoints help you:

- Understand program execution.
- Inspect variable values.
- Find logical errors.
- Step through code line by line.
- Change variable values during execution.
- Test different scenarios.

---

## Advantages over print()

Instead of writing:

```python
print(x)
print(y)
print(result)
```

A breakpoint lets you inspect every variable instantly.

---

## Common Debugging Actions

- Continue execution
- Step Over
- Step Into
- Step Out
- Inspect Variables
- Watch Expressions
- Evaluate Expressions
- Change Variable Values

---

## Python Debugger (pdb)

Python uses the pdb debugger.

Calling

```python
breakpoint()
```

internally starts pdb (unless configured otherwise).

Equivalent to:

```python
import pdb
pdb.set_trace()
```

---

## Important Commands

| Command | Meaning |
|----------|---------|
| n | Next line |
| s | Step into function |
| c | Continue |
| q | Quit debugger |
| p variable | Print variable |
| l | Show nearby code |
| where | Show call stack |

---

## VS Code Shortcuts

| Action | Shortcut |
|----------|-----------|
| Toggle Breakpoint | F9 |
| Continue | F5 |
| Step Over | F10 |
| Step Into | F11 |
| Step Out | Shift+F11 |
| Restart | Ctrl+Shift+F5 |

---

## When to use Breakpoints

- Wrong output
- Unexpected values
- Loops behaving incorrectly
- Recursive functions
- API debugging
- Object inspection
- Data structure traversal

Breakpoints are one of the most powerful debugging tools available to programmers.