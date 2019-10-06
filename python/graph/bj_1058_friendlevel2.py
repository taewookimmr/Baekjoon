def solution():
    import sys
    n = int(input())
    graph = [[] for _ in range(n+1)]
    check = [0 for _ in range(n+1)]
    for v1 in range(n):
        mystring = sys.stdin.readline().rstrip()
        for v2, m in enumerate(mystring):
            if m == "Y":
                graph[v1].append(v2)
    
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