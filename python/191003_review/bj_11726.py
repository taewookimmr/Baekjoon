def solution():
    n = int(input())
    dp = {}
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-2]*2 + dp[i-3]
        
    print(dp[n]%10007)
solution()