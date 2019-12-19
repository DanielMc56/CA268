def detect_loop(lst):
    root = lst.head
    ptr = lst.head
    while ptr != None:
        if ptr.next == root:
            return True
        ptr = ptr.next
    return False