def maximum(lst):
    
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] < lst[1]:
            lst.pop(0)
        else:
            lst.pop(1)
        return maximum(lst)