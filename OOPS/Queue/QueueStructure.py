from OOPS.LinkedList.LinkedListNode import LinkedListNode
class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        node = LinkedListNode(data)
        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = node

    def dequeue(self):
        if self.first is None:
            return "Queue is empty"
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def printQueue(self):
        temp = self.first
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("empty")

    def peek(self):
        if self.first is None:
            return "Queue is empty"
        return self.first.data
    

    

    