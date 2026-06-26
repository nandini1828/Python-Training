from collections.exercises import (
    SimpleQueue,
    merge_tags
)


def test_queue():

    queue = SimpleQueue()

    queue.enqueue(10)

    assert queue.dequeue() == 10


def test_queue_size():

    queue = SimpleQueue()

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.size() == 2


def test_merge_tags():

    all_tags, common, only_a = merge_tags(
        ["Python", "AI"],
        ["python", "ML"]
    )

    assert "python" in common
    assert "ml" in all_tags