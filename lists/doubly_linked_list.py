from link import Link

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None

    def insertFirst(self, key, data):
        self.first = Link(key, data, self.first)
        if self.last == None:
            self.last = self.first
        else:
            self.first.next.prev = self.first

    def insertLast(self, key, data):
        self.last = Link(key, data, prev = self.last)
        if self.first == None:
            self.first = self.last
        else:
            self.last.prev.next = self.last

# TODO: corner cases
    def insertBefore(self, before, key, data):
        curr = self.first
        while curr != None:
            if curr.key == before:
                node = Link(key, data, curr, curr.prev)
                if curr == self.first:
                    self.first = node
                else:
                    node.prev.next = node
                curr.prev = node
                return
            curr = curr.next

# TODO: corner cases
    def insertAfter(self, after, key, data):
        curr = self.first
        while curr != None:
            if curr.key == after:
                node = Link(key, data, curr.next, curr)
                if curr == self.last:
                    self.last = node
                else:
                    node.next.prev = node
                curr.next = node
                return
            curr = curr.next

# TODO: corner cases
    def delete(self, key):
        curr = self.first
        while curr != None:
            if curr.key == key:
                if curr == self.last:
                    self.last = curr.prev
                else:
                    curr.next.prev = curr.prev
                if curr == self.first:
                    self.first = curr.next
                else:
                    curr.prev.next = curr.next
                return curr
            curr = curr.next
        return None

    def deleteLastEntry(self, key):
        curr = self.last
        while curr != None:
            if curr.key == key:
                if curr == self.last:
                    self.last = curr.prev
                else:
                    curr.next.prev = curr.prev
                if curr == self.first:
                    self.first = curr.next
                else:
                    curr.prev.next = curr.next
                return curr
            curr = curr.prev
        return None

    def deleteFirst(self):
        if self.isEmpty():
            return None
        elif self.first == self.last:
            node = self.first
            self.first = self.last = None
            return node
        else:
            node = self.first
            self.first = node.next
            self.first.prev = None
            return node


    def deleteLast(self):
        if self.isEmpty():
            return None
        elif self.first == self.last:
            node = self.first
            self.first = self.last = None
            return node
        else:
            node = self.last
            self.last = node.prev
            self.last.next = None
            return node

    def find(self, key):
        curr = self.first
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def findLastEntry(self, key):
        curr = self.last
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.prev
        return None

    def array(self):
        curr = self.first
        arr = []
        while(curr != None):
            arr.append(curr)
            curr = curr.next
        return arr

    def displayList(self):
        curr = self.first
        arr = []
        while(curr != None):
            print(curr)
            curr = curr.next
        return arr
