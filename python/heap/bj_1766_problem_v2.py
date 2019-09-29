MAX = 32000 + 1
adj = [[] for _ in range(MAX)]
visited = [False for  _ in range(MAX)]
indegree = [0 for  _ in range(MAX)]
order = [[] for  _ in range(MAX)]

def solution():
    import sys
    import heapq

    n, m =  list(map(int, sys.stdin.readline().split()))
    for i in range(0, m):
        prere, next = list(map(int, sys.stdin.readline().split()))
        heapq.heappush(adj[prere], next)
        indegree[next] += 1

    def orderingQuestion() :
        q = []
   
        for l in range(n):
            s = 0
            for i in range(1, n+1):
                if  visited[i] != True and indegree[i] == 0:
                    visited[i] = True
                    s= i
                    break

            if s != 0 :
                prere = s
                print(prere, end=' ')
                for i in range(len(adj[prere])):
                    if visited[adj[prere][i]] != True:
                        indegree[adj[prere][i]]-=1

    orderingQuestion()


solution()
			
