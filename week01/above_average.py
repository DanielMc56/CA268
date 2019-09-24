def above_average(numbers):

    total = 0
    for i in numbers:
        total += i
    lis = []  
    avg = total / len(numbers)
    for i in numbers:
    	if i > avg:
    		lis.append(i)
    return lis