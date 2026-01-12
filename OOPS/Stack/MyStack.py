from collections import deque
class MyStack(object):

    def __init__(self):
        self.pqueue = deque()
        self.squeue = deque()

    def push(self, x):
        if len(self.pqueue) == 0:
            self.pqueue.append(x)
        else:
            while(len(self.pqueue)!=0):
                self.squeue.append(self.pqueue.pop())

            self.pqueue.append(x)

            while(len(self.squeue)!=0):
                self.pqueue.append(self.squeue.pop())

    def pop(self):
        return self.pqueue.popleft()

    def top(self):
        if len(self.pqueue) > 0:
            return self.pqueue[0]
        return -1
            
    def empty(self):
        return len(self.pqueue) == 0

    def printStack(self):
        print(self.pqueue)