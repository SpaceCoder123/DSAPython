class MyHash:
    def __init__(self, bucketSize):
        self.bucketSize = bucketSize
        self.table = [None] * bucketSize  # Use None for empty slots

    def _hash(self, item): # method is for internal purposes for the class
        return item % self.bucketSize

    def search(self, item):
        index = self._hash(item)
        start_index = index  # Save the starting index

        while self.table[index] is not None:  # Stop if we find an empty slot (item not found)
            if self.table[index] == item:
                return item
            index = (index + 1) % self.bucketSize  # Linear probing (move to the next slot)

            if index == start_index: 
                return None
        return None  # Not found

    def insert(self, item):
        index = self._hash(item)
        start_index = index

        while self.table[index] is not None and self.table[index] != "deleted":
            if self.table[index] == item:
                return False  # Item already exists
            index = (index + 1) % self.bucketSize

            if index == start_index:
                return False  # Table is full

        self.table[index] = item
        return True

    def delete(self, item):
        index = self._hash(item)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == item:
                self.table[index] = "deleted"  # Mark slot as deleted
                return True
            index = (index + 1) % self.bucketSize

            if index == start_index:
                return False  # Item not found

        return False  # Item not found

    
h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.delete(56)
print(h.search(56))
h.delete(56)
print(h.table)