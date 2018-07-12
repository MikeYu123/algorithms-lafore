import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_first(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        self.assertEqual(list.first.key, 2)
        self.assertEqual(list.first.data["b"], 2)

    def test_insert_after(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertBefore(1, 3, {"c": 3})
        self.assertEqual(list.first.next.key, 3)
        self.assertEqual(list.first.next.data["c"], 3)
        self.assertEqual(list.first.next.next.key, 1)

    def test_insert_before(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertAfter(2, 3, {"c": 3})
        self.assertEqual(list.first.next.key, 3)
        self.assertEqual(list.first.next.data["c"], 3)
        self.assertEqual(list.first.next.next.key, 1)

    def test_insert_before_first(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertBefore(2, 3, {"c": 3})
        self.assertEqual(list.first.key, 3)
        self.assertEqual(list.first.data["c"], 3)
        self.assertEqual(list.first.next.key, 2)

    def test_find_existing(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertFirst(3, {"c": 3})
        self.assertEqual(list.find(2).data["b"], 2)

    def test_find_non_existing(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertFirst(3, {"c": 3})
        self.assertEqual(list.find(4), None)

    def test_delete_existing(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertFirst(3, {"c": 3})
        self.assertEqual(list.delete(4), None)
        self.assertEqual(len(list.array()), 3)

    def test_delete_non_existing(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertFirst(3, {"c": 3})
        self.assertEqual(list.delete(2).data["b"], 2)
        self.assertEqual(len(list.array()), 2)

    def test_delete_from_empty(self):
        list = LinkedList()
        self.assertEqual(list.delete(4), None)

    def test_delete_first_empty(self):
        list = LinkedList()
        self.assertEqual(list.deleteFirst(), None)

    def test_delete_first_non_empty(self):
        list = LinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        self.assertEqual(list.deleteFirst().data["b"], 2)
        self.assertEqual(len(list.array()), 1)
