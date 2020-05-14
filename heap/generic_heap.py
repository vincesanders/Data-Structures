import math
class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if comparator:
            self.comparator = comparator
        else:
            self.comparator = lambda x, y: x >= y

    def insert(self, value):
        #insert to rightmost spot.
        self.storage.append(value)
        index = len(self.storage) - 1
        self.heapify(index)

    def heapify(self, index):
        while index > 0:
            parentIndex = math.floor((index - 1) / 2) # index / 2 is not right on rightmost node
            #compare value to parent.
            x = self.storage[index]
            y = self.storage[parentIndex] # parent
            if self.comparator(x, y):
                self._bubble_up(index)
            else:
                return
            index = parentIndex

    def delete(self):
        value = self.storage.pop(0)
        self._sift_down(0)
        return value

    def get_priority(self):
        pass

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        value = self.storage[math.floor((index - 1) / 2)]
        self.storage[math.floor((index - 1) / 2)] = self.storage[index]
        self.storage[index] = value

    def _sift_down(self, index):
        child1_index = (index + 1) * 2
        child2_index = child1_index - 1
        if child1_index > self.get_size() - 1 < child2_index:
            return
        elif child1_index > self.get_size() - 1:
            if self.comparator(self.storage[child2_index], self.storage[index]):
                self._bubble_up(child2_index)
            return
        #if child 1 is larger than child 2
        if self.comparator(self.storage[child1_index], self.storage[child2_index]):
            # if child 1 is larger than parent
            if self.comparator(self.storage[child1_index], self.storage[index]):
                self._bubble_up(child1_index)
                self._sift_down(child1_index)
        else:
            if self.comparator(self.storage[child2_index], self.storage[index]):
                self._bubble_up(child2_index)
                self._sift_down(child2_index)

heap = Heap()

heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)

new_array = []
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
new_array.append(heap.delete())
print(new_array)