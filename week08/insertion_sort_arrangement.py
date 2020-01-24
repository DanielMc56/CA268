#
#   Return an empty list to get your list of numbers.
#
#   Then return a list of lists corresponding to the passes of an insertion sort on the numbers.
#   [11,17,15,13,6,8]
def solution():
    return [
        [11, 17],
        [11, 15, 17],
        [11, 13, 15, 17],
        [6, 11, 13, 15, 17],
        [6, 8, 11, 13, 15, 17],
    ]