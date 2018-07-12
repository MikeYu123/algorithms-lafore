import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_first(self):
        list = DoublyLinkedList()
        list.insertFirst(1, {"a": 1})
        list.insertFirst(2, {"b": 2})
        list.insertFirst(3, {"c": 3})
        list.insertFirst(4, {"d": 4})
        self.assertEqual(len(list.array()), 4)
        self.assertEqual(list.first.key, 4)
        self.assertEqual(list.last.key, 1)

    def test_insert_last(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertLast(3, {"c": 3})
        list.insertLast(4, {"d": 4})
        self.assertEqual(len(list.array()), 4)
        self.assertEqual(list.first.key, 1)
        self.assertEqual(list.last.key, 4)

    def test_insert_before1(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertBefore(2, 3, {"c": 3})
        self.assertEqual(len(list.array()), 3)
        self.assertEqual(list.first.key, 1)
        self.assertEqual(list.first.next.key, 3)
        self.assertEqual(list.last.key, 2)

    def test_insert_before2(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertBefore(1, 3, {"c": 3})
        self.assertEqual(len(list.array()), 3)
        self.assertEqual(list.first.key, 3)
        self.assertEqual(list.first.next.key, 1)
        self.assertEqual(list.last.key, 2)

    def test_insert_after1(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(1, 3,  {"c": 3})
        self.assertEqual(len(list.array()), 3)
        self.assertEqual(list.first.key, 1)
        self.assertEqual(list.first.next.key, 3)
        self.assertEqual(list.last.key, 2)

    def test_insert_after2(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(len(list.array()), 3)
        self.assertEqual(list.first.key, 1)
        self.assertEqual(list.first.next.key, 2)
        self.assertEqual(list.last.key, 3)

    def test_find_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.find(3).data["c"], 3)

    def test_find_non_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.find(4), None)

    def test_delete_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.delete(3).data["c"], 3)
        self.assertEqual(len(list.array()), 2)

    def test_delete_non_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.delete(4), None)
        self.assertEqual(len(list.array()), 3)


# TODO backward-iterators tests
    def test_find_last_entry_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertLast(2, {"с": 3})
        self.assertEqual(list.findLastEntry(2).data["c"], 3)

    def test_find_last_entry_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertLast(2, {"с": 3})
        self.assertEqual(list.findLastEntry(3), None)

    def test_delete_last_entry_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 2,  {"c": 3})
        self.assertEqual(list.deleteLastEntry(2).data["c"], 3)
        self.assertEqual(len(list.array()), 2)

    def test_delete_last_entry_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 2,  {"c": 3})
        self.assertEqual(list.deleteLastEntry(3), None)

    def test_delete_first_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.deleteFirst().data['a'], 1)
        self.assertEqual(len(list.array()), 2)

    def test_delete_first_non_existing(self):
        list = DoublyLinkedList()
        self.assertEqual(list.deleteFirst(), None)

    def test_delete_last_existing(self):
        list = DoublyLinkedList()
        list.insertLast(1, {"a": 1})
        list.insertLast(2, {"b": 2})
        list.insertAfter(2, 3,  {"c": 3})
        self.assertEqual(list.deleteLast().data['c'], 3)
        self.assertEqual(len(list.array()), 2)

    def test_delete_last_non_existing(self):
        list = DoublyLinkedList()
        self.assertEqual(list.deleteLast(), None)
