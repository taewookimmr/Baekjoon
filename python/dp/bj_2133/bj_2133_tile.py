def solution():
    n = int(input())
    if n%2 :
        return 0
    if n==2:
        return 3
    if n==4:
        return 11
    
    dp = [0 for e in range(n+1)]
    dp[0]=1
    dp[2]=3
    dp[4]=11
    for i in range(6, n+1, 2):
        j = 2
        while True:
            if i-j >= 0:
                dp[i] += dp[i-j]*(3 if j==2 else 2)
                j+=2
            else:
                break
    print(dp[n])

solution()
