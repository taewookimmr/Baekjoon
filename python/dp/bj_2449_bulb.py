
def solution():
    import sys
    sys.setrecursionlimit(10**6)
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    bulb = list(map(int, sys.stdin.readline().rstrip().split()))    
    bulb.insert(0, -1) # insert dummy 
    
    MAX = 201
    INF = 2**20
    dp = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    
    def recur(a,b, depth):
        # print("depth : ", depth , a, b)
        if a==b: 
            return 0
        if dp[a][b] != -1: 
            return dp[a][b]
        dp[a][b] = INF
        for i in range(a,b):
            temp = 0 if bulb[a] == bulb[i+1] else 1 
            dp[a][b] = min(dp[a][b], recur(a,i, depth+1)+recur(i+1,b, depth+1)+temp)
        return dp[a][b]
    
    print(recur(1, n, 1))
                        
  
def solution_good():
    import sys

    bulb_num, color_num = map(int, input().split())
    bulbs = list(map(int, input().split()))
    dp = [[0] * bulb_num for _ in range(bulb_num)]

    for i in range(bulb_num):
        for j in reversed(range(i)):
            min_count = sys.maxsize
            for k in range(j, i):
                sub_count = dp[j][k] + dp[k + 1][i]

                if bulbs[k] != bulbs[i]:
                    sub_count += 1

                if sub_count < min_count:
                    min_count = sub_count
            dp[j][i] = min_count

    print(dp[0][-1])      
    
                
solution()
        
    