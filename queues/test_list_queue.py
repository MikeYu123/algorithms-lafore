import unittest
from list_queue import ListQueue

class TestListQueue(unittest.TestCase):
    def test_insert_one(self):
        queue = ListQueue()
        queue.insert(1)
        self.assertEqual(queue.list(), [1])

    def test_insert_two(self):
        queue = ListQueue()
        queue.insert(1)
        queue.insert(2)
        self.assertEqual(queue.list(), [1, 2])

    def test_head_empty(self):
        queue = ListQueue()
        with self.assertRaises(ValueError):
            queue.head()

    def test_head_non_empty(self):
        queue = ListQueue()
        queue.insert(1)
        self.assertEqual(queue.head(), 1)

    def test_insert_until_full(self):
        queue = ListQueue(5)
        for i in range(5):
            queue.insert(i)
        self.assertEqual(queue.list(), [0, 1, 2, 3, 4])

    def test_insert_two_then_remove(self):
        queue = ListQueue()
        queue.insert(1)
        queue.insert(2)
        res = queue.remove()
        self.assertEqual(res, 1)
        self.assertEqual(queue.list(), [2])

    def test_remove_empty(self):
        queue = ListQueue()
        with self.assertRaises(ValueError):
            res = queue.remove()

    def test_is_empty_when_empty(self):
        queue = ListQueue()
        self.assertTrue(queue.isEmpty())

    def test_is_empty_when_inserted(self):
        queue = ListQueue()
        queue.insert(1)
        self.assertFalse(queue.isEmpty())

    def test_is_empty_when_inserted_and_deleted(self):
        queue = ListQueue()
        queue.insert(1)
        queue.remove()
        self.assertTrue(queue.isEmpty())

if __name__ == '__main__':
    unittest.main()
