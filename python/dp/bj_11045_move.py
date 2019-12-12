import time

def solution():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))

    r,c = getline()
    g=[]
    for _ in range(r):
        g.append(getline())
        
    s= time.time()  
    for _ in range(100000):
        dp=[[0 for _ in range(c)] for _ in range(r)]
        dp[0][0]=g[0][0]
        dirs = [[1,0],[0,1], [1,1]]
        for i in range(r):
            for j in range(c):
                for dr, dc in dirs:
                    if i+dr < r and j+dc < c :
                        dp[i+dr][j+dc] = max(dp[i+dr][j+dc], g[i+dr][j+dc]+dp[i][j])
    e = time.time()
    print("delta= ", e-s)
    print(dp[-1][-1])
    
    
def solution_good():
    import sys
    In = sys.stdin.readline

    n,m=map(int,In().split())
    dp=[[*map(int,In().split())] for _ in range(n)]
    s = time.time()
    for _ in range(100000):
        for i in range(1, n):
            dp[i][0] += dp[i-1][0]
        for i in range(1, m):
            dp[0][i] += dp[0][i-1]

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i-1][j])
    e = time.time()
    print("delta= ", e-s)   
    print(dp[-1][-1]) 


solution()
solution_good()


                    
            
            