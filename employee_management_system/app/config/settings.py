"""Application settings and data file paths."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
EMPLOYEES_JSON_PATH = DATA_DIR / "employees.json"
DEPARTMENTS_JSON_PATH = DATA_DIR / "departments.json"
EMPLOYEES_CSV_PATH = DATA_DIR / "employees.csv"
