# 02_loop_foundations

## What this project is about
This project teaches you how loops help a program repeat actions. In the guessing game, the program keeps asking until the user guesses correctly or runs out of turns.

## Why this topic matters
Loops are used everywhere:
- Repeating a task many times
- Checking user input again and again
- Processing items in a list or range

## Topic notes

### 1. while loops
A `while` loop repeats as long as a condition stays true.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

The loop keeps going until the condition becomes false.

### 2. for loops
A `for` loop is helpful when you already know what you want to repeat.

```python
for number in range(3):
    print(number)
```

This is often used with a range of numbers or a list.

### 3. break
`break` stops the loop immediately.

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

Use `break` when you no longer need to continue.

### 4. continue
`continue` skips the current step and moves to the next one.

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

This is useful when you want to ignore one specific case.

### 5. pass
`pass` does nothing. It is often used as a placeholder while you are building code.

```python
for number in range(3):
    if number == 1:
        pass
    else:
        print(number)
```

### 6. for-else and while-else
The `else` part runs when the loop finishes normally, without `break`.

```python
for number in range(3):
    print(number)
else:
    print("Loop finished normally")
```

## What this project demonstrates
- Repeating actions using loops
- Stopping a loop early with `break`
- Skipping parts of a loop with `continue`
- Using `pass` as a placeholder

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Understand how loops repeat code
- Learn the difference between `for` and `while`
- Practice controlling loop behavior clearly
