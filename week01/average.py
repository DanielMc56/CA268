def calc_average(numbers):

    total = 0
    for i in numbers:
        total += i

    avg = total / len(numbers)
    return avg
