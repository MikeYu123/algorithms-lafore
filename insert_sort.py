class InsertSort:
    def sort(self, array):
        a = array[:]
        l = len(a)
        for i in range(1, l):
            j = i - 1
            x = a[i]
            while (j >= 0 and a[j] > x):
                a[j+1] = a[j]
                j -= 1
            a[j + 1] = x
        return a
