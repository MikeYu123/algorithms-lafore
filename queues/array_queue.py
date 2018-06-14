class ArrayQueue:
    def __init__(self, size = 10):
        self.array = [None] * size
        self.size = size
        self.min = 0
        self.max = 0

    def isEmpty(self):
        return self.min == self.max

    def head(self):
        if self.isFull():
            raise ValueError("Reading head from empty queue")
        return self.array[self.min % self.size]

    def isFull(self):
        return (self.max > self.min) and ((self.max - self.min) % self.size == 0)

    def insert(self, element):
        if self.isFull():
            raise ValueError("Adding to full queue")
        self.array[self.max % self.size] = element
        self.max += 1

    def remove(self):
        if (self.isEmpty()):
            raise ValueError("Removing from empty queue")
        element = self.array[self.min % self.size]
        self.min += 1
        return element

    # Used only for testing
    def list(self):
        return self.array[self.min:self.max]
