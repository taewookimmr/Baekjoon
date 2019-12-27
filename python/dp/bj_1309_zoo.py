def solution():
    n = int(input())    
    dp = [1,1,1]
    for i in range(1, n):
        a = dp[0] + dp[1] + dp[2]
        b = dp[0] + dp[2]
        c = dp[0] + dp[1]
        dp = [a,b,c]
    print(sum(dp)%9901)
solution()