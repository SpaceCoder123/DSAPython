from collections import deque
class MinStack(object):
    def __init__(self):
        self.pqueue = deque()

    def push(self, x):
        if len(self.pqueue) == 0:
            self.pqueue.append((x,x))
        else:
            top, low = self.topElement()
            if x < low:
                self.pqueue.append((x,x))
            else:
                self.pqueue.append((x,low))
        return

    def pop(self):
        return self.pqueue.pop()

    def topElement(self):
        if len(self.pqueue) > 0:
            return self.pqueue[len(self.pqueue)-1]
        return -1

    def top(self):
        if len(self.pqueue) > 0:
            return self.pqueue[len(self.pqueue)-1][0]
        return -1
            
    def empty(self):
        return len(self.pqueue) == 0

    def printStack(self):
        print(self.pqueue)

    def getMin(self):
        top, min = self.topElement()
        return min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()