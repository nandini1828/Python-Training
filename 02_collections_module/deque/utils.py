from collections import deque


def queue_demo():

    queue = deque()

    queue.append("Task1")
    queue.append("Task2")
    queue.append("Task3")

    print(queue)

    print(queue.popleft())

    print(queue)