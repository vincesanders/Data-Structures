from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        def search_tree(node):
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    return True # break out of recursion
                else:
                    return search_tree(node.left)
            # elif value > node.value:
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    return True
                else:
                    return search_tree(node.right)
            # else:
            #     return True
        return search_tree(node)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while current_node:
            if target is current_node.value:
                return True
            elif target < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
        # if target == self.value: #recursive solution
        #     return True
        # if target < self.value:
        #     if self.left:
        #         return self.left.contains(target)
        #     else:
        #         return False
        # else:
        #     if self.right:
        #         return self.right.contains(target)
        #     else:
        #         return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            fn(node.value)
        self.order(traverse)

    def order(self, fn):
        return fn(self)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        def traverse_in_order(node):
            if node.left:
                traverse_in_order(node.left)
            print(node.value)
            if node.right:
                traverse_in_order(node.right)
        if node is None:
            self.order(traverse_in_order)
        else:
            traverse_in_order(node) # start search from selected node

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.level_order_bft(node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.level_order_dft(node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        def traverse_pre_order(node, values=[]):
            values.append(node.value)
            if node.left:
                traverse_pre_order(node.left, values)
            if node.right:
                traverse_pre_order(node.right, values)
            return values
        pre_order_list = self.order(traverse_pre_order)
        for v in pre_order_list:
            print(v)
        return pre_order_list

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        def traverse_post_order(node, values=[]):
            if node.left:
                traverse_post_order(node.left, values)
            if node.right:
                traverse_post_order(node.right, values)
            values.append(node.value)
            return values
        post_order_list = self.order(traverse_post_order)
        for v in post_order_list:
            print(v)
        return post_order_list

    def level_order_bft(self, node):
        waiting = Queue()
        waiting.enqueue(node)
        while len(waiting) > 0:
            node = waiting.dequeue()
            print(node.value)
            if node.left:
                waiting.enqueue(node.left)
            if node.right:
                waiting.enqueue(node.right)

    def level_order_dft(self, node):
        waiting = Stack()
        waiting.push(node)
        while len(waiting) > 0:
            node = waiting.pop()
            print(node.value)
            if node.left:
                waiting.push(node.left)
            if node.right:
                waiting.push(node.right)