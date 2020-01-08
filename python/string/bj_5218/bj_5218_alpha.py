def solution():
    n = int(input())
    for _ in range(n):
        answer = []
        a,b = input().rstrip().split()
        for d,e in zip(a,b):
            d,e = ord(d), ord(e)
            answer.append(e-d if e>=d else 26+e-d)
        print("Distances:", " ".join([str(k) for k in answer]))
    

solution()