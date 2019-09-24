import sys

def sum_to_k(lst, k):

    lis = []
    for i in range(len(lst)):
       for j in range(len(lst)):
          if lst[i] + lst[j] == k and lst[i] not in lis and lst[j] not in lis:
            lis.append(lst[i])
            lis.append(lst[j])

    i = 0
    while i < len(lis):
    	print( lis[i], lis[i + 1])
    	i += 2
