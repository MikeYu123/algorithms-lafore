import unittest
from array import Array

class TestArray(unittest.TestCase):
    def test_put(self):
        array = Array(3)
        array.put(1,1)
        self.assertEqual(array.array, [None, 1, None])

    def test_put_out_of_bounds(self):
        array = Array(3)
        with self.assertRaises(IndexError):
            array.put(11,1)

    def test_get_existing(self):
        array = Array(3)
        array.put(1,1)
        self.assertEqual(array.get(1), 1)

    def test_get_non_existing(self):
        array = Array(3)
        array.put(1,1)
        self.assertEqual(array.get(2), None)

    def test_get_out_of_bounds(self):
        array = Array(3)
        array.put(1,1)
        with self.assertRaises(IndexError):
            array.get(11)

    def test_find_existing(self):
        array = Array(5)
        array.put(1,1)
        array.put(3,4)
        self.assertEqual(array.find(4), 3)

    def test_find_first(self):
        array = Array(5)
        array.put(1,1)
        array.put(3,1)
        self.assertEqual(array.find(1), 1)

    def test_find_non_existing(self):
        array = Array(5)
        array.put(1,1)
        array.put(3,1)
        self.assertEqual(array.find(5), -1)
