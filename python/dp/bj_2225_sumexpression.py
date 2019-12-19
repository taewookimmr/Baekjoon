def solution():
    n, k = list(map(int, input().split()))
    dp = [[1]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(2, k+1):
            temp = 0
            for e in range(0, i+1):
                temp += dp[i-e][j-1]
            dp[i][j] = temp
    # print(dp)            
    print(dp[-1][-1]%1000000000)
    
def solution_good():
    f = lambda x: x < 1 or x*f(x-1)
    n,k = map(int, input().split())
    print(f(n+k-1)//(f(n)*f(k-1))%1000000000)
    
solution()
solution_good()