# data_types_methods.py

# This script demonstrates basic data types in Python and common operations associated with them.

def run():
    title = "Data Types & Methods"
    description = "Demonstrates Python basic data types and common operations."

    int_value = 42
    int_examples = [
        f"int_value = {int_value}",
        f"str(int_value) = {str(int_value)}",
        f"abs(-10) = {abs(-10)}",
        f"pow(2, 3) = {pow(2, 3)}",
        f"10 // 3 = {10 // 3}",
        f"10 % 3 = {10 % 3}",
    ]

    float_value = 3.14159
    float_examples = [
        f"float_value = {float_value}",
        f"round(float_value, 2) = {round(float_value, 2)}",
        f"int(float_value) = {int(float_value)}",
        f"float_value.is_integer() = {float_value.is_integer()}",
        f"formatted = {float_value:.2f}",
    ]

    string_value = "Python Programming"
    string_examples = [
        f"string_value = '{string_value}'",
        f"len(string_value) = {len(string_value)}",
        f"string_value.lower() = {string_value.lower()}",
        f"string_value.upper() = {string_value.upper()}",
        f"string_value.replace('Python', 'Java') = {string_value.replace('Python', 'Java')}",
        f"'Python' in string_value = {'Python' in string_value}",
    ]

    bool_examples = [
        f"True and False = {True and False}",
        f"True or False = {True or False}",
        f"not True = {not True}",
        f"5 > 3 = {5 > 3}",
        f"bool(1) = {bool(1)}",
        f"bool('') = {bool('')}",
    ]

    list_example = ["apple", "banana", "orange"]
    list_examples = [
        f"list_example = {list_example}",
        f"list_example[0] = {list_example[0]}",
        f"list_example[-1] = {list_example[-1]}",
        f"len(list_example) = {len(list_example)}",
        f"'apple' in list_example = {'apple' in list_example}",
    ]

    tuple_example = (10, 20)
    tuple_examples = [
        f"tuple_example = {tuple_example}",
        f"tuple_example[0] = {tuple_example[0]}",
        f"tuple_example.count(10) = {tuple_example.count(10)}",
        f"tuple_example.index(20) = {tuple_example.index(20)}",
    ]

    dict_example = {"name": "Alice", "age": 20}
    dict_examples = [
        f"dict_example = {dict_example}",
        f"dict_example['name'] = {dict_example['name']}",
        f"dict_example.get('age') = {dict_example.get('age')}",
        f"'grade' in dict_example = {'grade' in dict_example}",
    ]

    set_example = {"apple", "banana", "orange"}
    set_examples = [
        f"set_example = {set_example}",
        f"'banana' in set_example = {'banana' in set_example}",
        f"union example = {set_example | {'grape'}}",
    ]

    details = [
        "### Integer examples",
        *int_examples,
        "",
        "### Float examples",
        *float_examples,
        "",
        "### String examples",
        *string_examples,
        "",
        "### Boolean examples",
        *bool_examples,
        "",
        "### List examples",
        *list_examples,
        "",
        "### Tuple examples",
        *tuple_examples,
        "",
        "### Dictionary examples",
        *dict_examples,
        "",
        "### Set examples",
        *set_examples,
    ]

    return {
        "title": title,
        "description": description,
        "details": "\n".join(details),
    }


if __name__ == "__main__":
    result = run()
    print(result["title"])
    print(result["description"])
    print(result["details"])
    print('\n' + str(dir(int)))  # Show available methods for int
