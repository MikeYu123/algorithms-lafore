import unittest
from list_stack import ListStack

class TestListStack(unittest.TestCase):
    def test_push_one(self):
        stack = ListStack()
        stack.push(1)
        self.assertEqual(stack.list(), [1])
        self.assertEqual(stack.peek(), 1)

    def test_push_two(self):
        stack = ListStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.list(), [2, 1])
        self.assertEqual(stack.peek(), 2)

    def test_peek_empty(self):
        stack = ListStack()
        with self.assertRaises(ValueError):
            stack.peek()

    def test_peek_non_empty(self):
        stack = ListStack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_push_until_full(self):
        stack = ListStack(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.list(), [4, 3, 2, 1, 0])

    def test_push_two_then_pop(self):
        stack = ListStack()
        stack.push(1)
        stack.push(2)
        res = stack.pop()
        self.assertEqual(res, 2)
        self.assertEqual(stack.list(), [1])

    def test_pop_empty(self):
        stack = ListStack()
        with self.assertRaises(ValueError):
            res = stack.pop()

    def test_is_empty_when_empty(self):
        stack = ListStack()
        self.assertTrue(stack.isEmpty())

    def test_is_empty_when_pushed(self):
        stack = ListStack()
        stack.push(1)
        self.assertFalse(stack.isEmpty())

    def test_is_empty_when_pushed_and_deleted(self):
        stack = ListStack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.isEmpty())

if __name__ == '__main__':
    unittest.main()
