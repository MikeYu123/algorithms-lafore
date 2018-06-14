import unittest
from insert_sort import InsertSort
from sort_test import SortTest

class TestInsertSort(SortTest, unittest.TestCase):
    sorter = InsertSort()

if __name__ == '__main__':
    unittest.main()
