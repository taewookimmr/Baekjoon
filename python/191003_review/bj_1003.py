def solution():

    n = int(input())
    
    for _ in range(n):
        dp = {}
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        dp[2] = [1, 1]
        m = int(input())
        for i in range(3, m+1):
            a = dp[i-1][0] + dp[i-2][0] 
            b = dp[i-1][1] + dp[i-2][1]
            dp[i] = [a,b]
        for num in dp[m]:
            print(num, end = " ")
        print()
    
solution()