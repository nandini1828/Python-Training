"""Main demo for the Python Data Types Mastery project.

This script imports and exercises the core primitives, collection utilities,
class helpers, and inspection utilities in a single runnable demonstration.
"""
from primitives.introspection import list_public_attributes
from primitives.casting import safe_cast, count_truthy_falsy
from primitives.dunder_examples import dunder_rewrites
from collection_utils.list_utils import SimpleQueue
from collection_utils.dict_utils import query_json
from collection_utils.set_utils import merge_tags
from collection_utils.tuple_utils import tuple_examples
from classes.computer import CPU, Computer
from classes.object_deconstructor import deconstruct_object
from classes.student import Student
from exercises.queue import demo_queue_operations
from exercises.tag_merger import demo_merge_tags
from exercises.nested_json_query_engine import demo_json_query
from exercises.word_counter import word_count
from inspectors.object_inspector import get_method_names, get_docstrings

def main():
    """Run demo operations for every imported helper and class."""
    print("Python Data Types Mastery Demo")
    print("=" * 72)

    student = Student("Eve", [95, 87, 92])
    print("1. Primitives and Introspection")
    print("   Public Student attrs:", list_public_attributes(student))
    print("   Dunder rewrites:", dunder_rewrites())
    print(
        "   Safe casts:",
        safe_cast("12.5", float),
        safe_cast("12.5", int),
        safe_cast("abc", int, 0),
    )
    print("   Truthiness counts:", count_truthy_falsy([0, "hello", [], None, True, 3.14]))
    print("   Demo queue operations:", demo_queue_operations())

    print("\n2. Collection Utilities")
    queue = SimpleQueue()
    queue.enqueue("first")
    queue.enqueue("second")
    print("   Queue size after enqueue:", queue.size())
    print("   Dequeue:", queue.dequeue())
    print("   Queue size after dequeue:", queue.size())
    print("   Query name:", query_json({"user": {"profile": {"name": "Alice"}}}, "user.profile.name"))
    print("   Query missing age default:", query_json({"user": {"profile": {"name": "Alice"}}}, "user.profile.age", 18))
    print("   Merge tags:", merge_tags(["Python", "AI", "Coding"], ["ai", "Data", "python"]))
    print("   Tuple examples:", tuple_examples())
    print("   Demo merge tags:", demo_merge_tags())
    print("   Demo json query:", demo_json_query())
    print("   Word count:", word_count("Hello, world! Hello Python."))
    print("\n3. Classes and Object Deconstruction")
    
    cpu = CPU(8)
    computer = Computer("Dell", cpu)
    print("   Computer state:", deconstruct_object(computer))
    print("   Student average grade:", student.average_grade())
    print("   Student average grade unbound:", Student.average_grade(student))

    print("\n4. Inspectors")
    print("   Student method names:", get_method_names(student))
    print("   Student docstrings:", get_docstrings(Student))


if __name__ == "__main__":
    main()

