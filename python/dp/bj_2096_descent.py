def solution_memory_excess():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
    
    n = int(input())
    ground = []
    for _ in range(n):
        ground.append(getline())
    dp = [[[0,0] for _ in range(3) ] for _ in range(n)] # 최소, 최대 
    dir = [-1,0,1]
    for i in range(n):
        for j in range(3):
            dp[i][j][0] = ground[i][j]
            dp[i][j][1] = ground[i][j]
            if i == 0 :
                continue
            else:
                temp_max = []
                temp_min = []
                for v in dir:
                    u = j+v
                    if u >= 0 and u < 3:
                        temp_min.append(dp[i-1][u][0])
                        temp_max.append(dp[i-1][u][1])
                dp[i][j][0] += min(temp_min)
                dp[i][j][1] += max(temp_max)
                
    m, M = list(zip(*dp[-1]))
    print(max(M), min(m))

def solution():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
    def getDProw():
        temp = []
        for e in getline():
            temp.append([e,e])
        return temp
    
    n = int(input())
    previous = []
    for i in range(n):
        present = getDProw()
        if i:
            for j in range(3):
                temp_max = []
                temp_min = []
                for v in  [-1,0,1]:
                    u = j+v
                    if u >= 0 and u < 3:
                        temp_min.append(previous[u][0])
                        temp_max.append(previous[u][1])
                present[j][0] += min(temp_min)
                present[j][1] += max(temp_max)

        previous= present
                
            
    m, M = list(zip(*previous))
    print(max(M), min(m))
            

def solution_brilliant():
    import sys
    input = sys.stdin.readline
    n = int(input())
    m, k, l = map(int, input().split())
    a, b, c = m, k, l
    for i in range(n-1):
        u, v, w = map(int, input().split())
        m, k, l = max(m, k) + u, max(m, k, l) + v, max(k, l) + w
        a, b, c = min(a, b) + u, min(a, b, c) + v, min(b, c) + w
    print(max(m, k, l), min(a, b, c))
    
solution()
