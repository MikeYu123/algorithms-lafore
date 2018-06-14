import unittest
from bubble_sort import BubbleSort
from sort_test import SortTest

class TestBubbleSort(SortTest, unittest.TestCase):
    sorter = BubbleSort()

if __name__ == '__main__':
    unittest.main()
