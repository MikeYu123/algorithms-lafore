import unittest
from sort_test import SortTest

class DummySorter:
    def sort(self, array):
        a = array
        a.sort()
        return a

class TestDummySorts(SortTest, unittest.TestCase):
    sorter = DummySorter()

if __name__ == '__main__':
    unittest.main()
