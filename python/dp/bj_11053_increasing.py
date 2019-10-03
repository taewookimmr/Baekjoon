def solution():
    n = int(input())
    import sys 
    arr = list(map(int,sys.stdin.readline().rstrip().split()))

    d = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j] and d[j] < d[i] + 1:
                d[j] = d[i] + 1
    print(max(d))

solution()