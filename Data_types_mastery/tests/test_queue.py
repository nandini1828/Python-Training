# BEFORE PYTEST

import unittest

from collection_utils.list_utils import SimpleQueue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):

        queue = SimpleQueue()

        queue.enqueue("Python")

        self.assertEqual(
            queue.size(),
            1
        )

    def test_dequeue(self):

        queue = SimpleQueue()

        queue.enqueue("Python")

        value = queue.dequeue()

        self.assertEqual(
            value,
            "Python"
        )

    def test_empty_queue(self):

        queue = SimpleQueue()

        self.assertIsNone(
            queue.dequeue()
        )


if __name__ == "__main__":
    unittest.main()



# AFTER PYTEST

from exercises.queue import (
    SimpleQueue
)


def test_enqueue():

    queue = SimpleQueue()

    queue.enqueue(
        "Python"
    )

    assert (
        queue.size()
        == 1
    )


def test_dequeue():

    queue = SimpleQueue()

    queue.enqueue(
        "Python"
    )

    value = queue.dequeue()

    assert (
        value
        == "Python"
    )


def test_empty_queue():

    queue = SimpleQueue()

    assert (
        queue.dequeue()
        is None
    )
