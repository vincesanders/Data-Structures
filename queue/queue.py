from singly_linked_list import LinkedList
from stack import Stack
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
class Queue: #FIFO
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)
2. Re-implement the Queue class, this time using the linked list implementation
    as the underlying storage structure.
    Make sure the Queue tests pass.
    class Queue: #FIFO
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
3. What is the difference between using an array vs. a linked list when 
    implementing a Queue?
    dequeue with an list is slower than with a linked list. Probably because all indexes 
    of the remaining elements had to be shifted.
Stretch: What if you could only use instances of your Stack class to implement the Queue?
        What would that look like? How many Stacks would you need? Try it!
"""
class Queue: #FIFO
    def __init__(self):
        self.size = 0
        self.storage = [Stack(), Stack()]
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage[0].push(value)

    def dequeue(self):
        if len(self.storage[0]) is 0 is len(self.storage[1]):
            return None
        elif len(self.storage[1]) is 0: # if stack 2 is empty
            while len(self.storage[0]) is not 1: # move all but last to stack 2
                self.storage[1].push(self.storage[0].pop())
            value = self.storage[0].pop() # remove the last
        else: # there are items in stack 2
            value = self.storage[1].pop()
        self.size -= 1
        return value