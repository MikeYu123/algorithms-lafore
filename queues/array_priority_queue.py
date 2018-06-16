class ArrayPriorityQueue:
    def __init__(self, size = 10):
        self.array = [None] * size
        self.size = size
        self.max = -1

    def isEmpty(self):
        return self.max == -1

    def head(self):
        if self.isEmpty():
            raise ValueError("Reading head from empty queue")
        return self.array[self.max]

    def isFull(self):
        return self.max == self.size - 1

    def insert(self, element):
        if self.isFull():
            raise ValueError("Adding to full queue")
        i = self.max
        while (i >= 0 and self.array[i] >= element):
            self.array[i + 1] = self.array[i]
            i -= 1
        self.array[i + 1] = element
        self.max += 1

    def remove(self):
        if (self.isEmpty()):
            raise ValueError("Removing from empty queue")
        element = self.array[self.max]
        self.max -= 1
        return element

    # Used only for testing
    def list(self):
        return self.array[0:self.max + 1]
