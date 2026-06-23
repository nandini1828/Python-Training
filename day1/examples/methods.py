"""
Collection Methods Demonstration
"""


def string_methods_demo() -> None:

    name = "karthik"

    print(name.upper())
    print(name.lower())
    print(name.title())
    print(name.replace("k", "c"))
    print(name.split("r"))
    print(name.find("t"))


def list_methods_demo() -> None:

    employees = [
        "Karthik",
        "Koushik",
        "Rajesh"
    ]

    employees.append("Anil")
    employees.insert(1, "Ramesh")

    print(employees)


def dictionary_methods_demo() -> None:

    student = {
        "name": "Karthik",
        "age": 21
    }

    print(student.keys())
    print(student.values())
    print(student.items())


if __name__ == "__main__":

    string_methods_demo()
    list_methods_demo()
    dictionary_methods_demo()