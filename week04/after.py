class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

#Count method
    def count(self):
        pointer = self.head
        count = 0
        while pointer != None:
            count += 1
            pointer = pointer.next
            return count
        return 0

#Contains method
    def contains(self, item):
        pointer = self.head
        while pointer != None:
            if pointer.item == item:
                return True
            pointer = pointer.next
        return False

#after method
    def after(self,item):
        pointer = self.head
        while pointer and pointer.item != item:
            pointer = pointer.next
        return pointer.next.item if pointer else None