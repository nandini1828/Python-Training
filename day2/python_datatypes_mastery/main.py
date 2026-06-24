"""
main.py

Entry point for Python Data Types Mastery Project.
"""

import argparse

from primitives import (
    ObjectInspector,
    SafeCaster,
    DunderExamples
)

from collections_utils import (
    ListUtils,
    DictUtils,
    SetUtils,
    TupleUtils
)

from exercises import (
    SimpleQueue,
    merge_tags,
    JsonQuery,
    WordCounter
)

from classes import (
    Student,
    CPU,
    Computer,
    deconstruct_object
)

from inspectors import (
    get_methods,
    get_methods_and_docs
)


def demonstrate_introspection() -> None:
    print("\n" + "=" * 50)
    print("INTROSPECTION")
    print("=" * 50)

    number = 100

    print("Value:", number)
    print("Type:", ObjectInspector.get_type(number))
    print("Memory ID:", ObjectInspector.get_id(number))
    print("Is int:", ObjectInspector.is_instance(number, int))

    print("\nFirst 10 Attributes:")
    print(ObjectInspector.get_attributes(number)[:10])


def demonstrate_casting() -> None:
    print("\n" + "=" * 50)
    print("TYPE CASTING")
    print("=" * 50)

    print(SafeCaster.cast("123", int))
    print(SafeCaster.cast("12.5", float))
    print(SafeCaster.cast("abc", int, default=0))


def demonstrate_dunders() -> None:
    print("\n" + "=" * 50)
    print("DUNDER METHODS")
    print("=" * 50)

    print("10 + 20 =", DunderExamples.addition(10, 20))
    print("10 == 10 =", DunderExamples.equality(10, 10))
    print("str(123) =", DunderExamples.string_representation(123))


def demonstrate_collections() -> None:
    print("\n" + "=" * 50)
    print("LIST METHODS")
    print("=" * 50)
    print(ListUtils.demonstrate())

    print("\n" + "=" * 50)
    print("DICT METHODS")
    print("=" * 50)
    print(DictUtils.demonstrate())

    print("\n" + "=" * 50)
    print("SET METHODS")
    print("=" * 50)
    print(SetUtils.demonstrate())

    print("\n" + "=" * 50)
    print("TUPLE METHODS")
    print("=" * 50)
    print(TupleUtils.demonstrate())


def demonstrate_queue() -> None:
    print("\n" + "=" * 50)
    print("QUEUE EXERCISE")
    print("=" * 50)

    queue = SimpleQueue()

    queue.enqueue("Python")
    queue.enqueue("AI")
    queue.enqueue("ML")

    print("Queue Size:", queue.size())
    print("Dequeued:", queue.dequeue())
    print("Queue Size:", queue.size())


def demonstrate_tags() -> None:
    print("\n" + "=" * 50)
    print("TAG MERGER")
    print("=" * 50)

    result = merge_tags(
        ["Python", "AI", "ML"],
        ["python", "Data", "AI"]
    )

    print(result)


def demonstrate_json_query() -> None:
    print("\n" + "=" * 50)
    print("JSON QUERY")
    print("=" * 50)

    data = {
        "user": {
            "profile": {
                "name": "Bhavya",
                "age": 22
            }
        }
    }

    print(JsonQuery.query(data, "user.profile.name"))
    print(JsonQuery.query(data, "user.profile.age"))


def demonstrate_word_counter() -> None:
    print("\n" + "=" * 50)
    print("WORD COUNTER")
    print("=" * 50)

    text = """
    Python is great.
    Python is powerful.
    AI is powerful.
    """

    print(WordCounter.count(text))


def demonstrate_classes() -> None:
    print("\n" + "=" * 50)
    print("CLASSES & OBJECTS")
    print("=" * 50)

    student = Student(
        "Bhavya",
        [90, 95, 85]
    )

    print("Student Name:", student.name)
    print("Average:", student.average_grade())

    print("\nStudent __dict__")
    print(student.__dict__)

    print("\nStudent Class __doc__")
    print(Student.__doc__)


def demonstrate_composition() -> None:
    print("\n" + "=" * 50)
    print("COMPOSITION")
    print("=" * 50)

    cpu = CPU(8)

    computer = Computer(
        "Dell",
        cpu
    )

    print(computer.__dict__)
    print(cpu.__dict__)


def demonstrate_deconstructor() -> None:
    print("\n" + "=" * 50)
    print("OBJECT DECONSTRUCTOR")
    print("=" * 50)

    computer = Computer(
        "Dell",
        CPU(8)
    )

    print(deconstruct_object(computer))


def demonstrate_method_inspection() -> None:
    print("\n" + "=" * 50)
    print("METHOD INSPECTION")
    print("=" * 50)

    methods = get_methods(list)

    print("First 10 Methods:")
    print(methods[:10])


def demonstrate_documentation_inspection() -> None:
    print("\n" + "=" * 50)
    print("METHODS + DOCUMENTATION")
    print("=" * 50)

    docs = get_methods_and_docs(list)

    for item in docs[:5]:
        print("\nMethod:", item["method"])
        print("Documentation:", item["doc"])


def run_all() -> None:
    demonstrate_introspection()
    demonstrate_casting()
    demonstrate_dunders()
    demonstrate_collections()
    demonstrate_queue()
    demonstrate_tags()
    demonstrate_json_query()
    demonstrate_word_counter()
    demonstrate_classes()
    demonstrate_composition()
    demonstrate_deconstructor()
    demonstrate_method_inspection()
    demonstrate_documentation_inspection()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Python Data Types Mastery Project"
    )

    parser.add_argument(
        "--section",
        type=str,
        default="all",
        help="""
        Available values:
        introspection
        casting
        dunder
        collections
        queue
        tags
        json
        words
        classes
        composition
        deconstructor
        methods
        docs
        all
        """
    )

    return parser.parse_args()


def main() -> None:

    args = parse_arguments()

    section = args.section.lower()

    if section == "introspection":
        demonstrate_introspection()

    elif section == "casting":
        demonstrate_casting()

    elif section == "dunder":
        demonstrate_dunders()

    elif section == "collections":
        demonstrate_collections()

    elif section == "queue":
        demonstrate_queue()

    elif section == "tags":
        demonstrate_tags()

    elif section == "json":
        demonstrate_json_query()

    elif section == "words":
        demonstrate_word_counter()

    elif section == "classes":
        demonstrate_classes()

    elif section == "composition":
        demonstrate_composition()

    elif section == "deconstructor":
        demonstrate_deconstructor()

    elif section == "methods":
        demonstrate_method_inspection()

    elif section == "docs":
        demonstrate_documentation_inspection()

    else:
        run_all()

    print("\nPROJECT EXECUTED SUCCESSFULLY")


if __name__ == "__main__":
    main()