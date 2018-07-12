class SortedArray:
    def __init__(self, size = 10):
        self.size = size
        self.array = [None] * size;
        self.length = 0;

    def put(self, value):
        if self.length == self.size:
            raise ValueError('Putting to full array')
        elif self.length == 0:
            self.array[0] = value
            self.length += 1
            return
        for i in range(self.length - 1, -1, -1):
            if self.array[i] > value:
                self.array[i+1] = self.array[i]
            else:
                self.array[i+1] = value
                self.length +=1
                return
        self.array[0] = value
        self.length += 1


    def get(self, index):
        if self.length <= index:
            raise IndexError('Index out of bounds')
        return self.array[index];

    def find(self, value):
        bottom = 0
        top = self.length - 1
        while bottom != top:
            middle = (bottom + top) // 2
            if self.array[middle] == value:
                return middle
            elif self.array[middle] > value:
                top = middle
            else:
                bottom = middle + 1
        return -1
