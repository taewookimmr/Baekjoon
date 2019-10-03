def solution():
    n = int(input())

    dp0 = {}
    dp1 = {}
    dp0[1] = 0
    dp1[1] = 1
    
    dp0[2] = 1
    dp1[2] = 0
    
    for i in range(3, n+1):
        dp0[i] = dp0[i-1] + dp1[i-1]
        dp1[i] = dp0[i-1]
        
    print(dp0[n] + dp1[n])
    
solution()