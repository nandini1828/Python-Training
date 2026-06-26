"""
main.py

Entry point for Python Concepts Training Project
"""

from Introspection.introspection import (
    get_object_type,
    get_object_id,
    inspect_object,
    list_public_attributes
)

from Introspection.exercises import (
    dunder_rewrite,
    demonstrate_naming_conventions
)

from type_casting.type_casting import (
    check_exact_type,
    check_instance,
    Animal,
    Dog,
    demonstrate_casting_examples
)

from type_casting.exercises import (
    count_truthy_falsy,
    safe_conversion_examples
)

from dictionary.dictionaries_json import (
    DictionaryOperations,
    JsonOperations
)

# Add these imports after creating collections/oop files
# from collections.exercises import SimpleQueue, merge_tags
# from oop_memory.exercises import deconstruct_object


def run_introspection_demo():

    print("\n" + "=" * 50)
    print("SECTION 1: INTROSPECTION")
    print("=" * 50)

    x = 100

    print("Type:", get_object_type(x))
    print("ID:", get_object_id(x))

    print("\nPublic Attributes:")
    print(list_public_attributes([])[:10])

    print("\nInspect Object:")
    print(inspect_object("Python"))

    print("\nDunder Rewrite:")
    print(dunder_rewrite())

    print("\nNaming Conventions:")
    print(demonstrate_naming_conventions())


def run_casting_demo():

    print("\n" + "=" * 50)
    print("SECTION 2: TYPE CASTING")
    print("=" * 50)

    dog = Dog()

    print(
        "Exact Type Check:",
        check_exact_type(dog, Animal)
    )

    print(
        "Instance Check:",
        check_instance(dog, Animal)
    )

    print("\nCasting Examples:")
    print(demonstrate_casting_examples())

    print("\nSafe Conversion Examples:")
    print(safe_conversion_examples())

    print("\nTruthiness Auditor:")
    print(
        count_truthy_falsy(
            [0, "", [], None, True, 3.14]
        )
    )


def run_dictionary_demo():

    print("\n" + "=" * 50)
    print("SECTION 4: DICTIONARIES & JSON")
    print("=" * 50)

    data = {
        "name": "Alice",
        "age": 22
    }

    print(
        "Get:",
        DictionaryOperations.get_value(
            data,
            "name"
        )
    )

    print(
        "Keys:",
        DictionaryOperations.get_keys(
            data
        )
    )

    print(
        "Values:",
        DictionaryOperations.get_values(
            data
        )
    )

    print(
        "Items:",
        DictionaryOperations.get_items(
            data
        )
    )

    json_string = """
    {
        "name": "Alice",
        "city": "Hyderabad"
    }
    """

    print("\nJSON To Dict:")
    print(
        JsonOperations.json_to_dictionary(
            json_string
        )
    )

    print(
        "\nValid JSON:",
        JsonOperations.is_valid_json(
            json_string
        )
    )


def main():

    run_introspection_demo()

    run_casting_demo()

    run_dictionary_demo()

    print("\nProject Execution Completed")


if __name__ == "__main__":
    main()