class BubbleSort:
    def sort(self, array):
        a = array[:]
        l = len(a)
        for i in range(l):
            for j in range(i + 1, l):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
        return a
