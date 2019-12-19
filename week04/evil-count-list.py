def even_count(lst):
    ptr = lst.head
    count = 0
    while ptr != None:
        if ptr.item % 2 == 0:
            count += 1
        ptr = ptr.next
    return count