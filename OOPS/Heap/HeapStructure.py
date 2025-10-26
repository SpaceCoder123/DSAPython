
class HeapStructure:
    def __init__(self):
        self.root = []
    
    def insert(self, value):
        self.root.append(value)
        self.heapify()

    def heapify(self):
        n = len(self.root)
        currIdx = n - 1
        parent = (currIdx-1)//2
        while(currIdx > 0):
            if self.root[parent] > self.root[currIdx]:
                self.root[parent],self.root[currIdx]=self.root[currIdx], self.root[parent]
            currIdx = parent
            parent = (currIdx-1)//2

    def rootHeapify(self, index):
        n = len(self.root)
        parent = index
        while True:
            leftChild = 2 * parent + 1
            rightChild = 2 * parent + 2
            smallest = parent

            if leftChild < n and self.root[leftChild] < self.root[smallest]:
                smallest = leftChild
            if rightChild < n and self.root[rightChild] < self.root[smallest]:
                smallest = rightChild

            if smallest != parent:
                self.root[parent], self.root[smallest] = self.root[smallest], self.root[parent]
                parent = smallest
            else:
                break

    def minHeapify(self, idx):
        currIdx = idx
        parent = (currIdx-1)//2
        while(currIdx > 0):
            if self.root[parent] > self.root[currIdx]:
                self.root[parent],self.root[currIdx]=self.root[currIdx], self.root[parent]
            currIdx = parent
            parent = (currIdx-1)//2


    def printHeap(self):
        print(self.root)

    def deleteMin(self):
        n = len(self.root)
        self.root[0], self.root[n-1] = self.root[n-1], self.root[0]
        minValue = self.root.pop()
        self.rootHeapify(0)
        return minValue

if __name__ == "__main__":
    root = HeapStructure()
    root.insert(5)  
    root.insert(3)
    root.insert(8)
    root.insert(1)  
    root.insert(2)
    root.insert(9)        
    # root.printHeap()  
    root.deleteMin()
    root.printHeap()