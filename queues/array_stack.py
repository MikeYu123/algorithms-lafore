class ArrayStack:
    def __init__(self, size = 10):
        self.array = [None] * size
        self.size = size
        self.max = -1

    def isEmpty(self):
        return self.max == -1

    def peek(self):
        if self.isEmpty():
            raise ValueError("Peeking empty stack")
        return self.array[self.max]

    def isFull(self):
        return self.max == self.size - 1

    def push(self, element):
        if self.isFull():
            raise ValueError("Pushing to full stack")
        self.max += 1
        self.array[self.max] = element

    def pop(self):
        if (self.isEmpty()):
            raise ValueError("Popping from empty stack")
        element = self.array[self.max]
        self.max -= 1
        return element

    # Used only for testing
    def list(self):
        return self.array[0:self.max + 1]
