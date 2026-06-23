from collection_utils.list_utils import SimpleQueue


def demo_queue_operations():
    q = SimpleQueue()
    q.enqueue("first")
    q.enqueue("second")
    return q.dequeue(), q.size()
