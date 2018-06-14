import unittest
from array_queue import ArrayQueue

class TestArrayQueue(unittest.TestCase):
    def test_insert_one(self):
        queue = ArrayQueue()
        queue.insert(1)
        self.assertEqual(queue.list(), [1])

    def test_insert_two(self):
        queue = ArrayQueue()
        queue.insert(1)
        queue.insert(2)
        self.assertEqual(queue.list(), [1, 2])

    def test_head_empty(self):
        queue = ArrayQueue()
        with self.assertRaises(ValueError):
            queue.head()

    def test_insert_until_full(self):
        queue = ArrayQueue(5)
        for i in range(5):
            queue.insert(i)
        self.assertEqual(queue.list(), [0, 1, 2, 3, 4])

    def test_insert_to_full(self):
        queue = ArrayQueue(5)
        for i in range(5):
            queue.insert(i)
        with self.assertRaises(ValueError):
            queue.insert(5)

    def test_insert_two_then_remove(self):
        queue = ArrayQueue()
        queue.insert(1)
        queue.insert(2)
        res = queue.remove()
        self.assertEqual(res, 1)
        self.assertEqual(queue.list(), [2])

    def test_remove_empty(self):
        queue = ArrayQueue()
        with self.assertRaises(ValueError):
            res = queue.remove()

    def test_is_empty_when_empty(self):
        queue = ArrayQueue()
        self.assertTrue(queue.isEmpty())

    def test_is_empty_when_inserted(self):
        queue = ArrayQueue()
        queue.insert(1)
        self.assertFalse(queue.isEmpty())

    def test_is_empty_when_inserted_and_deleted(self):
        queue = ArrayQueue()
        queue.insert(1)
        queue.remove()
        self.assertTrue(queue.isEmpty())

if __name__ == '__main__':
    unittest.main()
