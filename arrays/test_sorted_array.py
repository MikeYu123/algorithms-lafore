import unittest
from sorted_array import SortedArray

class TestSortedArray(unittest.TestCase):
    def test_put_to_top(self):
        array = SortedArray(5)
        array.put(1)
        array.put(2)
        array.put(3)
        self.assertEqual(array.array, [1,2,3,None,None])

    def test_put_to_middle(self):
        array = SortedArray(5)
        array.put(1)
        array.put(5)
        array.put(3)
        self.assertEqual(array.array, [1,3,5,None,None])

    def test_put_to_bottom(self):
        array = SortedArray(5)
        array.put(3)
        array.put(5)
        array.put(1)
        self.assertEqual(array.array, [1,3,5,None,None])

    def test_put_to_full(self):
        array = SortedArray(3)
        array.put(1)
        array.put(5)
        array.put(3)
        with self.assertRaises(ValueError):
            array.put(4)

    def test_get_existing(self):
        array = SortedArray(3)
        array.put(1)
        array.put(5)
        array.put(3)
        self.assertEqual(array.get(1), 3)

    def test_get_out_of_bounds(self):
        array = SortedArray(5)
        array.put(1)
        array.put(5)
        array.put(3)
        with self.assertRaises(IndexError):
            array.get(4)

    def test_find_existing(self):
        array = SortedArray(5)
        array.put(1)
        array.put(5)
        array.put(3)
        self.assertEqual(array.find(3), 1)

    def test_find_non_existing(self):
        array = SortedArray(5)
        array.put(1)
        array.put(5)
        array.put(3)
        self.assertEqual(array.find(4), -1)
