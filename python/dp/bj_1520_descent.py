def solution():
    import sys
    sys.setrecursionlimit(10**6)
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
        
    r, c = getline()
    dp = [[0 for _ in range(c)] for _ in range(r)]
    ck = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0]=1
    
    ground = []
    for _ in range(r):
        ground.append(getline())
        
    def recursive(rr, cc):
        for v in [1, -1]:
            if rr+v < r and rr+v>=0 and ground[rr][cc] < ground[rr+v][cc]:
                if dp[rr+v][cc] or ck[rr+v][cc]:
                    dp[rr][cc] += dp[rr+v][cc]
                else:
                    dp[rr][cc] +=recursive(rr+v,cc)
            if cc+v < c and cc+v>=0 and ground[rr][cc] < ground[rr][cc+v]:
                if dp[rr][cc+v] or ck[rr][cc+v]:
                    dp[rr][cc] += dp[rr][cc+v]
                else:
                    dp[rr][cc] +=recursive(rr,cc+v)
        ck[rr][cc]=1
        return dp[rr][cc]
    
    recursive(r-1, c-1)
    print(dp[-1][-1])


solution()

