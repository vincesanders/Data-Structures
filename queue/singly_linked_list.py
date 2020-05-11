class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'Node: value-{self.value} next-{self.next}'
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        # set this node's next reference to the passed in node
        self.next = new_next

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1
    def __str__(self):
        if self.is_empty():
            return '[]'
        string = '['
        current_node = self.head
        while current_node.next != None:
            string += str(current_node.value) + ', '
            current_node = current_node.next
        string += str(current_node.value) + ']'
        return string
    def is_empty(self):
        return self.head == None
    def add_to_tail(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return True
        elif self.head.value == None:
            self.head.value = value
            return True
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return True
    def prepend(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return True
        if self.head.value == None:
            self.head.value = value
            return True
        new_node = Node(value)
        head = self.head
        new_node.next = head
        self.head = new_node
        self.size += 1
    def add_at_index(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.size:
            raise Exception("Sorry, that index is not in the list.")
        elif index == self.size - 1:
            self.add_to_tail(value)
        new_node = Node(value)
        current_index = 1
        current_node = self.head
        while current_index != index:
            current_node = current_node.next
            current_index += 1
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1
        return True
    def remove(self, value):
        if self.is_empty():
            raise Exception("Sorry, the list is empty.")
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return value
        current_node = self.head
        while current_node != None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.size -= 1
                return value
            current_node = current_node.next
    def remove_head(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return value
    def get_nth_to_last(self, n):
        if self.is_empty():
            raise Exception("Sorry, the list is empty.")
        left_node = self.head
        distance = 0
        right_node = self.head
        while right_node.next != None and distance < n - 1:
            right_node = right_node.next
            distance += 1
        if distance != n - 1:
            return None
        while right_node.next != None:
            left_node = left_node.next
            right_node = right_node.next
        return left_node.value
    def contains(self, value):
        if self.is_empty():
            return False
        current_node = self.head
        while current_node.next != None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        if current_node.value == value:
            return True
        return False
    def get_max(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            return self.head.value
        current_node = self.head
        current_max = self.head.value
        while current_node.next != None:
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        if current_node.value > current_max:
            current_max = current_node.value
        return current_max