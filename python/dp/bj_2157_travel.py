def solution_recursive():
    import sys 
    def getline():
        return list(map(int,sys.stdin.readline().rstrip().split()))
    n, m, k = getline()
    dic = {}
    for _ in range(k):
        a,b,c = getline()
        if a<b:
            a-=1
            b-=1
            d = a*n+b
            if d in dic.keys():
                dic[d] = max(dic[d], c)         
            else :
                dic[d] = c     
    info = list(dic.items())
    temp = [] 
    for d, c in info:
        temp.append([d//n, d%n, c])
    info = temp
    dp = [0 for _ in range(n)]
    
    def recursive(s, accum, depth):
        if depth <= m:
            for start, end, weight in info:
                    if s== start and dp[end] < accum+weight:
                        dp[end] = accum+weight
                        if end != n-1:
                            recursive(end,accum+weight,depth+1)
    recursive(0,0,1)
    print(dp[-1])

def solution():
    import sys 
    def getline():
        return list(map(int,sys.stdin.readline().rstrip().split()))
    n, m, k = getline()
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1 
    info = []
    for _ in range(k):
         a,b, c = getline()
         if a<b :
             info.append([a,b,c,])
    info.sort()         
    for a,b,c in info:
        for d in range(1, m):
            if  d+1 <= m and dp[a][d]:
                dp[b][d+1] = max(dp[b][d+1], dp[a][d]+c)
    print(max(dp[-1])-1)
    
solution()
            