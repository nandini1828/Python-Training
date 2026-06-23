<<<<<<< HEAD
import unittest

from day2.core.queue import (
    SimpleQueue
)


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
=======
from collection_utils.list_utils import SimpleQueue


def test_simple_queue():
    q = SimpleQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.dequeue() == 2
>>>>>>> 6dd5e5f (Pushing structured code)
