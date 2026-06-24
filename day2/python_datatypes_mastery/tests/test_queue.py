from exercises import SimpleQueue


def test_enqueue():

    queue = SimpleQueue()

    queue.enqueue("Python")

    assert queue.size() == 1


def test_dequeue():

    queue = SimpleQueue()

    queue.enqueue("Python")

    assert queue.dequeue() == "Python"


def test_queue_size():

    queue = SimpleQueue()

    queue.enqueue("A")
    queue.enqueue("B")

    assert queue.size() == 2