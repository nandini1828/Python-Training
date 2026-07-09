import pandas as pd
import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.filtering import DataFiltering

df = pd.read_csv("data/sample_data.csv")

print("\nSingle Column")
print(DataFiltering.select_column(df, "Name"))

print("\nMultiple Columns")
print(DataFiltering.select_columns(df, ["Name", "Salary"]))

print("\nloc")
print(DataFiltering.select_with_loc(df, 0))

print("\niloc")
print(DataFiltering.select_with_iloc(df, 2))

print("\nAge > 30")
print(DataFiltering.filter_age(df, 30))

print("\nIT Department")
print(DataFiltering.filter_department(df, "IT"))