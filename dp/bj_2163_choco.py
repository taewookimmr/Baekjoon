import sys 
def solution():
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = i-1
    for i in range(1, m+1):
        dp[1][i] = i-1

    for i in range(2, n+1):
        for j in range(2, m+1):
            min = 1000000000000000
            for k in range(1, i): 
                if min > dp[k][j] + dp[i-k][j]+1:
                    min = dp[k][j] + dp[i-k][j]+1
            for k in range(1, j):
                if min > dp[i][k] + dp[i][j-k]+1:
                    min = dp[i][k] + dp[i][j-k]+1

            dp[i][j] = min
    print(dp[n][m])

import sys 
def solution2():
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    minim = min(n,m)
    maxim = max(n,m)
    print((minim-1) + minim*(maxim-1))

solution2()


solution()
