"""
solution.py

Solutions for the Pandas Core Concepts practice questions.
"""

from model import PandasData


def solution_1():
    print("\nSolution 1")
    df = PandasData.employees()
    print(df)


def solution_2():
    print("\nSolution 2")
    df = PandasData.employees()
    print(df.head(3))


def solution_3():
    print("\nSolution 3")
    df = PandasData.employees()
    print(df.tail(2))


def solution_4():
    print("\nSolution 4")
    df = PandasData.employees()
    print("Shape:", df.shape)


def solution_5():
    print("\nSolution 5")
    df = PandasData.employees()
    print(df["Name"])


def solution_6():
    print("\nSolution 6")
    df = PandasData.employees()
    print(df[["Name", "Salary"]])


def solution_7():
    print("\nSolution 7")
    df = PandasData.employees()
    print(df[df["Salary"] > 50000])


def solution_8():
    print("\nSolution 8")
    df = PandasData.employees()
    print(df[df["Department"] == "IT"])


def solution_9():
    print("\nSolution 9")
    df = PandasData.employees()
    print(df.sort_values(by="Salary", ascending=False))


def solution_10():
    print("\nSolution 10")
    df = PandasData.employees()
    print(df.groupby("Department")["Salary"].mean())


def solution_11():
    print("\nSolution 11")
    df = PandasData.employees()

    df["Bonus"] = df["Salary"] * 0.10
    print(df)


def solution_12():
    print("\nSolution 12")
    df = PandasData.employees()

    df = df.rename(columns={"Salary": "Monthly_Salary"})
    print(df)


def solution_13():
    print("\nSolution 13")
    df = PandasData.employees()

    print(df["Department"].unique())


def solution_14():
    print("\nSolution 14")
    df = PandasData.employees()

    print(df["Department"].value_counts())


def solution_15():
    print("\nSolution 15")
    df = PandasData.employees()

    df.to_csv("employee_output.csv", index=False)
    print("employee_output.csv created successfully.")


def run():
    solution_1()
    solution_2()
    solution_3()
    solution_4()
    solution_5()
    solution_6()
    solution_7()
    solution_8()
    solution_9()
    solution_10()
    solution_11()
    solution_12()
    solution_13()
    solution_14()
    solution_15()


if __name__ == "__main__":
    run()