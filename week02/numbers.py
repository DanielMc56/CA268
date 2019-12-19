def sum_to_k(lst, k):
    i = 0
    j = len(lst) - 1
    while i < len(lst) - 1:
        if i == j:
           return False
        elif lst[i] + lst[j] == k:
            return True
        elif lst[i] + lst[j] < k:
            i += 1
        elif lst[i] + lst[j] > k:
            j -= 1
    return False    

print(sum_to_k([5, 10], 15))
print(sum_to_k([7], 14))
print(sum_to_k([7, 7], 14))
print(sum_to_k([3, 7, 13], 14))
#True
print(sum_to_k([5, 10], 13))
#False
print(sum_to_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))
#True
print(sum_to_k([2, 4, 6, 8, 10, 12], 13))
#False
print(sum_to_k([2, 4, 6, 8, 10, 12], 14))
#True
print(sum_to_k([2, 4, 6, 8, 10, 12], 16))
#True
print(sum_to_k([1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 40], 41))