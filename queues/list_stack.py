from linked_list import LinkedList

class ListStack:
    # TODO limit size
    def __init__(self, size = 0):
        self.list_obj = LinkedList()

# top of the stack is
    def list(self):
        return [link.key for link in self.list_obj.array()]

    def isEmpty(self):
        return self.list_obj.isEmpty()

    def push(self, key):
        self.list_obj.insertFirst(key, None)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Popping from empty stack")
        return self.list_obj.deleteFirst().key

    def peek(self):
        if self.isEmpty():
            raise ValueError("Peeking from empty stack")
        return self.list_obj.first.key
