def solution():
    import sys
    sys.setrecursionlimit(100000)
    
    n = int(input())
    
    if n == 1:
        print(0)
        return

    parent = list(map(int, sys.stdin.readline().rstrip().split()))

    graph = [[] for _ in range(n)]
    for c, p in enumerate(parent):
        if p != -1:
            graph[p].append(c)
    
    target = int(input())
    start = graph.pop(target)
    graph.insert(target, [-1]) # [-1] mean it is deleted node 
    
    for g in graph:
        if target in g:
            g.remove(target)
    
    def recursive(e):
        if len(e):
            for target in e:
                for g in graph:
                    if target in g:
                        g.remove(target)
                temp = graph.pop(target)
                graph.insert(target, [-1])
                recursive(temp)
    recursive(start)
    count = 0
    for g in graph:
        if len(g) == 0:
            count += 1
    print(graph)            
    print(count)

solution()