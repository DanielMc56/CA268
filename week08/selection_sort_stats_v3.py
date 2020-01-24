def selection_sort(lst):
    lo = 0
    hi = len(lst) - 1
    compares = 0
    moves = 0
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            compares += 1
            if lst[j] < lst[min_index]:
                min_index = j
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                compares += 1
            else:
                compares += 1

        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        moves += 3
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        moves += 3
        lo += 1
        hi -= 1
    return compares, moves