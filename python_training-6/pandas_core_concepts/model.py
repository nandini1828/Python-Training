"""
Sample datasets used across all Pandas examples.
"""

import pandas as pd


class PandasData:

    @staticmethod
    def employees():
        return pd.DataFrame({
            "ID": [101, 102, 103, 104, 105],
            "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
            "Age": [25, 30, 28, 35, 29],
            "Department": ["HR", "IT", "IT", "Finance", "HR"],
            "Salary": [40000, 60000, 55000, 70000, 45000],
            "City": ["Hyderabad", "Bangalore", "Hyderabad", "Chennai", "Bangalore"]
        })

    @staticmethod
    def students():
        return pd.DataFrame({
            "RollNo": [1, 2, 3, 4, 5],
            "Name": ["Anil", "Bhavna", "Charan", "Deepa", "Esha"],
            "Marks": [85, 90, 76, 88, 95],
            "Grade": ["A", "A", "B", "A", "A"]
        })

    @staticmethod
    def sales():
        return pd.DataFrame({
            "OrderID": [1001, 1002, 1003, 1004, 1005],
            "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
            "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
            "Quantity": [2, 5, 3, 1, 4],
            "Price": [65000, 500, 1500, 70000, 550]
        })