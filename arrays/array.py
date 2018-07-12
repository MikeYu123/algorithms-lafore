class Array:
    def __init__(self, size = 10):
        self.size = size
        self.array = [None] * size;

    def put(self, index, value):
        if self.size <= index:
            raise IndexError('Index out of bounds')
        self.array[index] = value

    def get(self, index):
        if self.size <= index:
            raise IndexError('Index out of bounds')
        return self.array[index];

    def find(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1
