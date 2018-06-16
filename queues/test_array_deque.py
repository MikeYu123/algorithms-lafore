import unittest
from array_deque import ArrayDeque

# TODO still screwed up :(
class TestArrayDeque(unittest.TestCase):
    def test_insert_one(self):
        deque = ArrayDeque()
        deque.insert(1)
        self.assertEqual(deque.list(), [1])

    def test_push_one(self):
        deque = ArrayDeque()
        deque.push(1)
        self.assertEqual(deque.list(), [1])

    def test_insert_two(self):
        deque = ArrayDeque()
        deque.insert(1)
        deque.insert(2)
        self.assertEqual(deque.list(), [1, 2])

    def test_push_two(self):
        deque = ArrayDeque()
        deque.push(1)
        deque.push(2)
        self.assertEqual(deque.list(), [2, 1])

    def test_head_empty(self):
        deque = ArrayDeque()
        with self.assertRaises(ValueError):
            deque.head()

    def test_head_non_empty(self):
        deque = ArrayDeque()
        deque.push(1)
        self.assertEqual(deque.head(), 1)

    def test_peek_empty(self):
        deque = ArrayDeque()
        with self.assertRaises(ValueError):
            deque.peek()

    def test_peek_non_empty(self):
        deque = ArrayDeque()
        deque.insert(1)
        self.assertEqual(deque.peek(), 1)

    def test_push_full(self):
        deque = ArrayDeque(5)
        [deque.insert(i) for i in range(5)]
        with self.assertRaises(ValueError):
            deque.push(1)

    def test_insert_full(self):
        deque = ArrayDeque(5)
        [deque.push(i) for i in range(5)]
        with self.assertRaises(ValueError):
            deque.insert(1)

    def test_composite1(self):
        deque = ArrayDeque()
        deque.push(1)
        deque.insert(2)
        deque.insert(3)
        deque.push(4)
        deque.insert(5)
        deque.push(6)
        self.assertEqual(deque.remove(), 5)
        deque.push(7)
        deque.insert(8)
        self.assertEqual(deque.pop(), 7)
        self.assertEqual(deque.list(), [6,4,1,2,3,8])

    def test_composite2(self):
        deque = ArrayDeque()
        deque.push(1)
        deque.push(2)
        self.assertEqual(deque.remove(), 1)
        self.assertEqual(deque.remove(), 2)


if __name__ == '__main__':
    unittest.main()
