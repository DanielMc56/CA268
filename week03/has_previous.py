def has_previous():
    
    seen = set()
    dups = []
    
    print("Enter numbers (-1 to end): ", end="")
    num = input().lstrip()
    
    while num != "-1":
        if num not in seen:
            seen.add(num)
        else:
            dups.append(num)
        num = input().lstrip()
    
    return (print(' '.join(dups) + " "))

print(has_previous())