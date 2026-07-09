import pandas as pd
import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.cleaning import DataCleaning

df = pd.read_csv("data/sample_data.csv")

print("Missing Values")
print(DataCleaning.missing_values(df))

print("\nBonus Column")
print(DataCleaning.add_bonus(df.copy()))

print("\nRename Column")
print(DataCleaning.rename_salary(df))

print("\nRemove Duplicates")
print(DataCleaning.remove_duplicates(df))