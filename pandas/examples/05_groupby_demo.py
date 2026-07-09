import pandas as pd
import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.grouping import DataGrouping

df = pd.read_csv("data/sample_data.csv")

print("Sorted by Salary")
print(DataGrouping.sort_salary(df))

print("\nAverage Salary")
print(DataGrouping.average_salary(df))

print("\nMaximum Salary")
print(DataGrouping.maximum_salary(df))

print("\nEmployee Count")
print(DataGrouping.employee_count(df))