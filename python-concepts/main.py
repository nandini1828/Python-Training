from section1.introspection import list_public_attributes
from section2.type_casting import safe_cast
from section3.collections import SimpleQueue
from section4.dictionaries_json import query_json
from section5.exercises import create_student_without_init


def main():

    print(safe_cast("12.5", float))

    queue = SimpleQueue()

    queue.enqueue(10)
    queue.enqueue(20)

    print(queue.dequeue())

    data = {
        "user": {
            "profile": {
                "name": "Alice"
            }
        }
    }

    print(query_json(data, "user.profile.name"))

    print(create_student_without_init())


if __name__ == "__main__":
    main()