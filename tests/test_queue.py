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