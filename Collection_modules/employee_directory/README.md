# Employee Directory

## What this project does
This project uses `defaultdict(list)` to store employee records grouped by department.

## Key concepts used
- `defaultdict(list)` automatically creates a new list when a new department is used.
- Employees are stored as tuples in the form `(name, department)`.

## Main features
- Add employees to a department.
- View all available departments.
- View all employees in a selected department.
- Search for an employee and find their department.
- Display the number of employees in each department.

## Why this is useful
This is a simple example of grouping related records together without writing extra checks for missing keys.
