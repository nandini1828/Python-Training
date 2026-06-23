from day1.utils.collection_utils import (
    CollectionUtility
)
from day2.core.queue import (
    SimpleQueue
)


def main():

    queue = SimpleQueue()

    queue.enqueue("Python")
    queue.enqueue("FastAPI")

    print(
        "Dequeued:",
        queue.dequeue()
    )

    result = CollectionUtility.merge_tags(
        ["python", "java"],
        ["python", "aws"]
    )

    print(result)


if __name__ == "__main__":
    main()