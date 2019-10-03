def solution():
    n = int(input())
    wine = [0]
    for _ in range(n):
        wine.append(int(input()))

    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    dp[1][0] = 0
    dp[1][1] = wine[1]
    dp[1][2] = 0
    
    for i in range(2, n+1):
        dp[i][0] = max([dp[i-1][j] for j in range(3)])
        dp[i][1] = dp[i-1][0] + wine[i]
        dp[i][2] = dp[i-1][1] + wine[i]
        
    print(max([dp[n][i] for i in range(3)]))
    
solution()
    