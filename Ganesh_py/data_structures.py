# data_structures.py

def run():
    title = "Data Structures"
    description = "Demonstrates stack, queue, linked list, binary search tree, and hash table usage."

    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop() if self.items else None

        def peek(self):
            return self.items[-1] if self.items else None

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)

    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.append(item)

        def dequeue(self):
            return self.items.pop(0) if self.items else None

        def peek(self):
            return self.items[0] if self.items else None

        def is_empty(self):
            return len(self.items) == 0

        def size(self):
            return len(self.items)

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def display(self):
            items = []
            current = self.head
            while current:
                items.append(str(current.data))
                current = current.next
            return " -> ".join(items)

        def insert_at_beginning(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        def remove(self, data):
            if not self.head:
                return
            if self.head.data == data:
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self._insert_recursive(self.root, value)

        def _insert_recursive(self, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    self._insert_recursive(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self._insert_recursive(node.right, value)

        def search(self, value):
            return self._search_recursive(self.root, value)

        def _search_recursive(self, node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            if value < node.value:
                return self._search_recursive(node.left, value)
            return self._search_recursive(node.right, value)

        def inorder_traversal(self):
            result = []
            self._inorder_recursive(self.root, result)
            return result

        def _inorder_recursive(self, node, result):
            if node:
                self._inorder_recursive(node.left, result)
                result.append(node.value)
                self._inorder_recursive(node.right, result)

    class HashTable:
        def __init__(self, size=10):
            self.size = size
            self.table = [[] for _ in range(size)]

        def _hash(self, key):
            return hash(key) % self.size

        def insert(self, key, value):
            index = self._hash(key)
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

        def search(self, key):
            index = self._hash(key)
            for k, v in self.table[index]:
                if k == key:
                    return v
            return None

        def delete(self, key):
            index = self._hash(key)
            self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.insert_at_beginning(5)
    linked_list.remove(20)

    bst = BinarySearchTree()
    for value in [50, 30, 70, 20, 40]:
        bst.insert(value)

    ht = HashTable()
    ht.insert("name", "Alice")
    ht.insert("age", 20)
    ht.insert("city", "New York")

    details = [
        "### Stack",
        f"peek = {stack.peek()}",
        f"pop = {stack.pop()}",
        f"size = {stack.size()}",
        "",
        "### Queue",
        f"peek = {queue.peek()}",
        f"dequeue = {queue.dequeue()}",
        f"size = {queue.size()}",
        "",
        "### LinkedList",
        f"display = {linked_list.display()}",
        "",
        "### Binary Search Tree",
        f"search 30 = {bst.search(30)}",
        f"search 100 = {bst.search(100)}",
        f"inorder_traversal = {bst.inorder_traversal()}",
        "",
        "### Hash Table",
        f"search name = {ht.search('name')}",
        f"search age = {ht.search('age')}",
    ]

    return {
        "title": title,
        "description": description,
        "details": "\n".join(details),
    }


if __name__ == "__main__":
    result = run()
    print(result["title"])
    print(result["description"])
    print(result["details"])
