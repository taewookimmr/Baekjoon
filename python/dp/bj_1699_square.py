def solution_recursive():
    n = int(input())
    dp = [0 for _ in range(n+1)]
    
    import math 
    m = math.floor(math.sqrt(n))
    for a in range(1, m+1):
        dp[a*a] =  1
        
    import sys
    sys.setrecursionlimit(10**6)
    
    def recur(m):
        if dp[m] == 0:
            temp = []
            for i in range(1, m):
                recur(i)
                recur(m-i)
                temp.append(dp[i]+dp[m-i])
            dp[m] = min(temp)
                
    recur(n)
    print(dp)
    print(dp[n])

def solution():
    n = int(input())
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        j = 2
        while j*j <=i :
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j+=1
    print(dp[n])

solution()