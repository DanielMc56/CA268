def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        compare = 0
        swap = 0
        for todo in range(1, len(lst)):
            i = todo
            compare += 1
            while i > 0 and lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
                i -= 1
                if i != 0:
                    compare += 1
                swap += 1
                
        return (compare, swap)