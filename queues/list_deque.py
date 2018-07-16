from doubly_linked_list import DoublyLinkedList

class ListDeque:
    # TODO limit size
    def __init__(self, size = 0):
        self.list_obj = DoublyLinkedList()

# top of the stack is
    def list(self):
        return [link.key for link in self.list_obj.array()]

    def isEmpty(self):
        return self.list_obj.isEmpty()

    def insert(self, key):
        self.list_obj.insertLast(key, None)

    def push(self, key):
        self.list_obj.insertFirst(key, None)

    def remove(self):
        if self.isEmpty():
            raise ValueError("Removing from empty deque")
        return self.list_obj.deleteFirst().key

    def pop(self):
        if self.isEmpty():
            raise ValueError("Popping from empty deque")
        return self.list_obj.deleteLast().key

    def head(self):
        if self.isEmpty():
            raise ValueError("Reading head from empty deque")
        return self.list_obj.first.key

    def peek(self):
        if self.isEmpty():
            raise ValueError("Peeking from empty deque")
        return self.list_obj.last.key
