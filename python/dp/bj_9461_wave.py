def solution():
    def wave(n):
        dp = [0,1,1,1,2,2,3,4,5,7,9]
        if n <= 10 :
            print(dp[n])
            return
        temp = [0]*(n-10)
        dp += temp
        
        for i in range(11, n+1):
            dp[i]=dp[i-1]+dp[i-5]
        print(dp[n])
        return 
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        wave(n)

solution()