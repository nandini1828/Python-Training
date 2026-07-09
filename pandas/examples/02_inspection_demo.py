import pandas as pd
import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.inspection import DataInspection

df = pd.read_csv("data/sample_data.csv")

print("\nHEAD")
DataInspection.display_head(df)

print("\nTAIL")
DataInspection.display_tail(df)

print("\nSHAPE")
DataInspection.display_shape(df)

print("\nINFO")
DataInspection.display_info(df)

print("\nSTATISTICS")
DataInspection.display_statistics(df)

print("\nVALUE COUNTS")
DataInspection.value_counts(df, "Department")

print("\nUNIQUE VALUES")
DataInspection.unique_values(df, "City")