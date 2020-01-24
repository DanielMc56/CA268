from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    def min_max_bucket_length(self):
        minimum = 0
        maximum = 0
        i = 0
        for items in self.table:
            if self.table[i] != None:
                if minimum == 0:
                    minimum = len(self.table[i])
                elif minimum > len(self.table[i]):
                    minimum = len(self.table[i])
                
                if maximum == 0:
                    maximum = len(self.table[i])
                elif maximum < len(self.table[i]):
                    maximum = len(self.table[i])
            i += 1
        
        return (minimum, maximum)