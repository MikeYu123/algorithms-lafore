from link import Link

class EndedLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first == None

    def insertFirst(self, key, data):
        second = self.first
        link = Link(key, data, second)
        self.first = link
        if self.last == None:
            self.last = link

    def insertLast(self, key, data):
        link = Link(key, data)
        if self.isEmpty():
            self.first = link
            self.last = link
        else:
            self.last.next = link
            self.last = link

    def deleteFirst(self):
        link = self.first
        if self.last == link:
            self.last = self.first = None
        else:
            self.first = link.next
        return link

    def insertAfter(self, after, key, data):
        curr = self.first
        while(curr != None):
            if curr.key == after:
                node = Link(key, data, curr.next)
                curr.next = node
                if node.next == None:
                    self.last = node
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

    def findLast(self, key):
        curr = self.last
        while(curr != None):
            if curr.key == key:
                return curr
            curr = curr.prev
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
