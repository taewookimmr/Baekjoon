def solution():
    n = int(input())
    
    point = [-1]
    for _ in range(n):
        point.append(int(input()))

    dp = [0 for _ in range(1+n)]
    dp[1] = point[1]
    dp[2] = point[1] + point[2]
    dp[3] = max(point[1] + point[3], point[2] + point[3])
    
    for i in range(4, n+1):
        way1 = dp[i-3] + point[i-1] + point[i]
        way2 = dp[i-2] + point[i]
        dp[i] = max(way1, way2)
    print(dp[n])
    
    
solution()
                
        
                         
        