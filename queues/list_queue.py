from ended_linked_list import EndedLinkedList

class ListQueue:
    # TODO limit size
    def __init__(self, size = 0):
        self.list_obj = EndedLinkedList()

# top of the stack is
    def list(self):
        return [link.key for link in self.list_obj.array()]

    def isEmpty(self):
        return self.list_obj.isEmpty()

    def insert(self, key):
        self.list_obj.insertLast(key, None)

    def remove(self):
        if self.isEmpty():
            raise ValueError("Removing from empty queue")
        return self.list_obj.deleteFirst().key

    def head(self):
        if self.isEmpty():
            raise ValueError("Reading head from empty queue")
        return self.list_obj.first.key
