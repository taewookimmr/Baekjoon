def solution():
    import sys
    n = int(input())
    src = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    Inf = 1001
    dp = [Inf]*(n)
    dp[0] = 0
    for i, e in enumerate(src):
        if e :
            for j in range(1, e+1):
                if i+j <n:
                    dp[i+j] = min(dp[i]+1, dp[i+j])
    if dp[-1] == Inf:
        print(-1)                    
    else:
        print(dp[-1])

solution()