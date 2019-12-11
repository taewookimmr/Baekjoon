def solution():
    import sys
    sys.setrecursionlimit(10**6)
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
        
    r, c = getline()
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0]=1
    
    ground = []
    for _ in range(r):
        ground.append(getline())
        
    count = [0]
    def recursive(rr, cc):
        if rr == r-1 and cc == c-1:
            count[-1] +=1 
            return 
        for v in [1, -1]:
            if rr+v < r and rr+v>=0 and ground[rr][cc] > ground[rr+v][cc]:
                recursive(rr+v,cc)
            if cc+v < c and cc+v>=0 and ground[rr][cc] > ground[rr][cc+v]:
                recursive(rr,cc+v)
    recursive(0,0)
    print(count[-1])


solution()

