class SortTest:
    def test_non_empty_1(self):
        self.assertEqual(self.sorter.sort([2,3,1]), [1,2,3])

    def test_non_empty_2(self):
        self.assertEqual(self.sorter.sort([4,1,2,-4,6,3,5]), [-4,1,2,3,4,5,6])

    def test_strings(self):
        self.assertEqual(self.sorter.sort(['3', '1','2', 'a', '11']), ['1', '11', '2', '3', 'a'])

    def test_empty(self):
        self.assertEqual(self.sorter.sort([]), [])
