def solution():
    import sys
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    
    ground = [] 
    for _ in range(n):
        ground.append(list(map(int, sys.stdin.readline().rstrip())))
        
    dp = [[1 if ground[r][c] else 0 for c in range(m)] for r in range(n)]
    
    for r in range(1,n):
        for c in range(1,m):
            if dp[r-1][c-1] and dp[r-1][c] and dp[r][c-1]:
                dp[r][c]=min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
    
    answer = max([max([dp[r][c] for c in range(m)]) for r in range(n)])
    print(answer**2)
        
    
solution()