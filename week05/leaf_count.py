class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def rcount_leaves(self, ptr):
        if ptr == None:
            return 0
        elif ptr.left == None and ptr.right == None:
            return 1 + self.rcount_leaves(ptr.left) + self.rcount_leaves(ptr.right)
        return self.rcount_leaves(ptr.left) + self.rcount_leaves(ptr.right)

    def count_leaves(self):
        return self.rcount_leaves(self.root)