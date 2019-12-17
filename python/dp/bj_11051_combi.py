def solution():
    import sys
    n,k = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = [[1 for _  in range(k+1)] for _ in  range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1, k+1):
            if i-1>= j:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    
    print(dp[n][k]%10007)

def solution_notdp():
    n,k=map(int,input().split())
    ans=1
    for i in range(k):
        ans*=n-i
    for i in range(k):
        ans//=k-i
    print(ans%10007)
         
solution()        