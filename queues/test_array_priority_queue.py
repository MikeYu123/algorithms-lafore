import unittest
from array_priority_queue import ArrayPriorityQueue

class TestArrayPriorityQueue(unittest.TestCase):
    def test_insert_one(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        self.assertEqual(queue.list(), [1])

    def test_insert_two(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        queue.insert(2)
        self.assertEqual(queue.list(), [1, 2])

    def test_head_empty(self):
        queue = ArrayPriorityQueue()
        with self.assertRaises(ValueError):
            queue.head()

    def test_head_non_empty1(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        self.assertEqual(queue.head(), 1)

    def test_head_non_empty2(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        queue.insert(3)
        queue.insert(2)
        self.assertEqual(queue.head(), 3)

    def test_insert_until_full(self):
        queue = ArrayPriorityQueue(5)
        for i in range(5):
            queue.insert(i)
        self.assertEqual(queue.list(), [0, 1, 2, 3, 4])

    def test_insert_to_full(self):
        queue = ArrayPriorityQueue(5)
        for i in range(5):
            queue.insert(i)
        with self.assertRaises(ValueError):
            queue.insert(5)

    def test_insert_random_to_sorted(self):
        queue = ArrayPriorityQueue()
        for i in range(3):
            queue.insert(i)
        queue.insert(1)
        self.assertEqual(queue.list(), [0, 1, 1, 2])

    def test_insert_two_then_remove(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        queue.insert(2)
        res = queue.remove()
        self.assertEqual(res, 2)
        self.assertEqual(queue.list(), [1])

    def test_remove_empty(self):
        queue = ArrayPriorityQueue()
        with self.assertRaises(ValueError):
            res = queue.remove()

    def test_is_empty_when_empty(self):
        queue = ArrayPriorityQueue()
        self.assertTrue(queue.isEmpty())

    def test_is_empty_when_inserted(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        self.assertFalse(queue.isEmpty())

    def test_is_empty_when_inserted_and_deleted(self):
        queue = ArrayPriorityQueue()
        queue.insert(1)
        queue.remove()
        self.assertTrue(queue.isEmpty())

if __name__ == '__main__':
    unittest.main()
