def solution():
    import sys
    import heapq
    v, e = list(map(int, sys.stdin.readline().split()))
    adj = [[0 for i in range(v)] for _ in range(v)]
    for i in range(e):
        v1, v2, t12, t21 = list(map(int, sys.stdin.readline().split()))
        adj[v1-1][v2-1] = t12
        adj[v2-1][v1-1] = t21

     
    


solution()

