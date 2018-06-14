import unittest
from array_stack import ArrayStack

class TestArrayStack(unittest.TestCase):
    def test_push_one(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertEqual(stack.list(), [1])
        self.assertEqual(stack.peek(), 1)

    def test_push_two(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.list(), [1, 2])
        self.assertEqual(stack.peek(), 2)

    def test_push_until_full(self):
        stack = ArrayStack(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.list(), [0, 1, 2, 3, 4])

    def test_push_to_full(self):
        stack = ArrayStack(5)
        for i in range(5):
            stack.push(i)
        with self.assertRaises(ValueError):
            stack.push(5)

    def test_push_two_then_pop(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)
        res = stack.pop()
        self.assertEqual(res, 2)
        self.assertEqual(stack.list(), [1])

    def test_pop_empty(self):
        stack = ArrayStack()
        with self.assertRaises(ValueError):
            res = stack.pop()

    def test_is_empty_when_empty(self):
        stack = ArrayStack()
        self.assertTrue(stack.isEmpty())

    def test_is_empty_when_pushed(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertFalse(stack.isEmpty())

    def test_is_empty_when_pushed_and_deleted(self):
        stack = ArrayStack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.isEmpty())

if __name__ == '__main__':
    unittest.main()
