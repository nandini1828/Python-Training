import pandas as pd
import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.combining import DataCombining

employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

salaries = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [50000, 70000, 80000]
})

merged = DataCombining.merge_dataframes(
    employees,
    salaries,
    "ID"
)

print("Merged DataFrame")
print(merged)

print("\nConcatenated DataFrame")

df1 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"]})

print(DataCombining.concatenate(df1, df2))