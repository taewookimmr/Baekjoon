def solution():
    n = int(input())
    import sys 
    arr = list(map(int,sys.stdin.readline().rstrip().split()))

    d = [arr[i] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                if d[j] < d[i] + arr[j] :
                    d[j] = d[i] + arr[j]
    print(max(d))

solution()