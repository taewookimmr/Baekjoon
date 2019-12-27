def solution():
    n = int(input())
    def body():
        m = int(input())
        dp = [0]*((3 if m<4 else m)+1)
        dp[1]=1
        dp[2]=dp[1]+1
        dp[3]=dp[1]+dp[2]+1
        if m<4:
            return dp[m]
        for i in range(4, m+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[-1])
        
    for _ in range(n):
        body()


solution()