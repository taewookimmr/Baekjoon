def solution():
    n = int(input())

    if n == 1: 
        print(10)
        return

    dp = [[e for e in range(10)] for _ in range(n)]
    for i in range(10):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(10):
            dp[i][j] = sum([dp[i-1][k] for k in range(j+1)])
    
    print(sum(dp[n-1]))

solution()
    


