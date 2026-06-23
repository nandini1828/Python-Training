"""
Python Data Types: The Exhaustive Mastery Guide
Main Driver Program
"""

# Section 1
from section1 import (
    inspect_object,
    list_public_attributes,
    dunder_rewrite
)

# Section 2
from section2 import (
    safe_cast,
    count_truthy_falsy
)

# Section 3
from section3 import (
    SimpleQueue,
    merge_tags
)

# Section 4
from section4 import (
    query_json,
    word_count
)

# Section 5
from section5 import (
    Student,
    create_student_without_init,
    deconstruct_object
)


def run_section1():

    print("\n" + "=" * 50)
    print("SECTION 1: INTROSPECTION")
    print("=" * 50)

    number = 100

    print("\nInspect Object:")
    print(inspect_object(number))

    print("\nPublic Attributes:")
    print(list_public_attributes("Python"))

    print("\nDunder Rewrite:")
    print(dunder_rewrite())


def run_section2():

    print("\n" + "=" * 50)
    print("SECTION 2: TYPE CHECKING & CASTING")
    print("=" * 50)

    print("\nSafe Casting:")

    print(
        safe_cast(
            "12.5",
            float
        )
    )

    print(
        safe_cast(
            "12.5",
            int
        )
    )

    print(
        safe_cast(
            "abc",
            int,
            default=0
        )
    )

    items = [
        0,
        "hello",
        [],
        None,
        True,
        3.14
    ]

    print("\nTruthy/Falsy Count:")
    print(count_truthy_falsy(items))


def run_section3():

    print("\n" + "=" * 50)
    print("SECTION 3: LISTS, TUPLES & SETS")
    print("=" * 50)

    queue = SimpleQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("\nQueue Size:")
    print(queue.size())

    print("\nDequeued Item:")
    print(queue.dequeue())

    print("\nQueue Size:")
    print(queue.size())

    tags_a = [
        "Python",
        "Java",
        "AI"
    ]

    tags_b = [
        "python",
        "ML",
        "AI"
    ]

    print("\nMerged Tags:")
    print(
        merge_tags(
            tags_a,
            tags_b
        )
    )


def run_section4():

    print("\n" + "=" * 50)
    print("SECTION 4: DICTIONARIES & JSON")
    print("=" * 50)

    data = {
        "user": {
            "profile": {
                "name": "Alice"
            }
        }
    }

    print("\nQuery JSON:")
    print(
        query_json(
            data,
            "user.profile.name"
        )
    )

    print(
        query_json(
            data,
            "user.profile.age",
            18
        )
    )

    text = """
    Python is great.
    Python is easy!
    """

    print("\nWord Count:")
    print(word_count(text))


def run_section5():

    print("\n" + "=" * 50)
    print("SECTION 5: CLASSES & MEMORY")
    print("=" * 50)

    student = Student(
        "Vyshu",
        [90, 95, 85]
    )

    print("\nStudent Dictionary:")
    print(student.__dict__)

    print("\nAverage Grade:")
    print(student.average_grade())

    print("\nCreate Student Without __init__:")
    print(create_student_without_init())

    print("\nDeconstruct Object:")
    print(
        deconstruct_object(
            student
        )
    )


def main():

    run_section1()

    run_section2()

    run_section3()

    run_section4()

    run_section5()

    print("\n" + "=" * 50)
    print("ALL SECTIONS EXECUTED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()