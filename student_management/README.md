# Student Management Learning API

This is a fresher-level FastAPI project focused on Python basics through a simple student management example.

## Topics Covered

- Built-in data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict`, `None`
- `dir()`, `type()`, and `isinstance()`
- Type casting and safe casting
- Truthiness
- Lists, tuples, sets, dictionaries, and JSON
- Classes, objects, methods, `self`, and composition
- Dunder methods: `__str__` and `__len__`
- Naming conventions
- Type annotations
- `argparse`

## Run the API

```bash
cd student_management
.venv/bin/uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Try the CLI

```bash
cd student_management
.venv/bin/python -m app.cli.student_cli --name Asha --age 20 --city Pune
```

## Main API Groups

- `/students` - create, read, update, delete students; includes class, object, method, `self`, composition, truthiness, dunder, and introspection examples
- `/courses` - create, read, update, delete courses and enroll students; includes list, tuple, set, dictionary, JSON, type casting, safe casting, and type hint examples

## Student APIs

- `GET /students/`
- `GET /students/{student_id}`
- `POST /students/`
- `PUT /students/{student_id}`
- `DELETE /students/{student_id}`

Create student body:

```json
{
  "name": "Asha",
  "age": 20,
  "city": "Pune"
}
```

## Course APIs

- `GET /courses/`
- `GET /courses/{course_id}`
- `POST /courses/`
- `PUT /courses/{course_id}`
- `DELETE /courses/{course_id}`
- `POST /courses/enroll`

Create course body:

```json
{
  "name": "FastAPI Basics",
  "duration_weeks": 3
}
```

Enroll course body:

```json
{
  "course_id": 1,
  "student_id": 1
}
```
