def solution():
    a = [e for e in range(10)]
    b = [e if e%2 == 0 else None for e in a]
    print(a)
    print(b)

solution()