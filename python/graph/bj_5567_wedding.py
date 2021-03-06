def solution():
    import sys
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    for _ in range(m):
        v1, v2 = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    queue = []
    queue.append([1, 0]) # index, level
    while len(queue):
        node, level = queue.pop(0) 
        check[node] = 1
        for n in graph[node]:
            if check[n] == 0 and level <2:
                queue.append([n, level+1])
    print(sum(check)-1)
    
    
        
        

solution()