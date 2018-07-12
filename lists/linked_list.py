from link import Link

class LinkedList:
    def __init__(self):
        self.first = None

    def insertFirst(self, key, data):
        second = self.first
        self.first = Link(key, data, second)

    def isEmpty(self):
        return self.first == None

    def deleteFirst(self):
        if self.isEmpty():
            return None
        node = self.first
        self.first = node.next
        return node

    def insertAfter(self, after, key, data):
        curr = self.first
        while(curr != None):
            if curr.key == after:
                node = Link(key, data, curr.next)
                curr.next = node
                return
            curr = curr.next
        raise ValueError("No key found")

    def insertBefore(self, before, key, data):
        prev, curr = None, self.first
        while(curr != None):
            if curr.key == before:
                node = Link(key, data, curr)
                if prev == None:
                    self.first = node
                else:
                    prev.next = node
                return
            prev = curr
            curr = curr.next
        raise ValueError("No key found")

    def find(self, key):
        curr = self.first
        while(curr != None):
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def delete(self, key):
        prev, curr = None, self.first
        while(curr != None):
            if curr.key == key:
                prev.next = curr.next
                return curr
            prev, curr = curr, curr.next
        return None

    def displayList(self):
        curr = self.first
        while(curr != None):
            print(curr.data)
            curr = curr.next

    def array(self):
        curr = self.first
        arr = []
        while(curr != None):
            arr.append(curr)
            curr = curr.next
        return arr
