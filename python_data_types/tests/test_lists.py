from lists import SimpleQueue, append_item


def test_append():
    lst = [1, 2]
    append_item(lst, 3)
    assert lst == [1, 2, 3]


def test_queue():
    q = SimpleQueue()
    q.enqueue("A")
    q.enqueue("B")

    assert q.dequeue() == "A"
    assert q.size() == 1