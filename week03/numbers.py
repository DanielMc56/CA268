import sys

def get_odd_list():
    lis = []
    for num in sys.stdin:
        num = num.strip()
        if num == "-1":
            break
        elif int(num) % 2 != 0:
            lis.append(int(num))
    return lis

print(get_odd_list())