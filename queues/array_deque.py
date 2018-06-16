class ArrayDeque:
    def __init__(self, size = 10):
        self.array = [None] * size
        self.size = size
        self.min = 0
        self.max = 0

    def isEmpty(self):
        return self.min == self.max

    def peek(self):
        if self.isEmpty():
            raise ValueError("Peeking from empty deque")
        return self.array[self.min % self.size]

    def head(self):
        if self.isEmpty():
            raise ValueError("Reading head from empty deque")
        return self.array[(self.max) - 1 % self.size]

    def isFull(self):
        return (self.max > self.min) and ((self.max - self.min) % self.size == 0)

    def insert(self, element):
        if self.isFull():
            raise ValueError("Inserting to full deque")
        self.array[self.max % self.size] = element
        self.max += 1

    def push(self, element):
        if self.isFull():
            raise ValueError("Pushing to full deque")
        self.min -= 1
        self.array[self.min % self.size] = element

    def pop(self):
        if (self.isEmpty()):
            raise ValueError("Popping from empty deque")
        element = self.array[self.min % self.size]
        self.min += 1
        return element

    def remove(self):
        if self.isEmpty():
            raise ValueError("Removing from empty deque")
        element = self.array[(self.max - 1) % self.size]
        self.max -= 1
        return element

    # Used only for testing
    def list(self):
        if self.min % self.size >= self.max % self.size:
            return self.array[self.min:] + self.array[:self.max]
        else:
            return self.array[self.min:self.max]
