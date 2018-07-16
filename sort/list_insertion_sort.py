from linked_list import LinkedList
from link import Link

class ListInsertionSort:
    def sort(self, array):
        list = LinkedList()
        for i in range(len(array)):
            if list.isEmpty():
                list.insertFirst(array[i], None)
            else:
                prev, curr = None, list.first
                while(curr != None and curr.key < array[i]):
                    prev, curr = curr, curr.next
                node = Link(array[i], None, curr)
                if prev == None:
                    list.first = node
                else:
                    prev.next = node
        return [link.key for link in list.array()]
