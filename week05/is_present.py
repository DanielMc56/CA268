class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
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

    #def count_even(self):
        #return self.recursive_count(self.head)

    #def recursive_count(self, ptr):
        #if ptr == None:
            #return 0
        #else:
            #if ptr.item % 2 == 0:
                #return 1 + self.recursive_count(ptr.next)
            #else:
                #return self.recursive_count(ptr.next)

    #def contains(self, item):
        #ptr = self.head
        #if ptr != None:
           # if ptr.item == item:
                #return True
            #else:
                #ptr = ptr.next
        #return False
    
    def is_present(self, word):
        return self.present(self.head, word)
    
    def present(self, ptr, word):
        if ptr != None:
            if ptr.item == word:
                return True
            return LinkedList.present(self, ptr.next, word)
        return False