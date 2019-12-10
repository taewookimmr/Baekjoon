def solution_memory_excess():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
    
    r, c = getline()
    array = []
    for _ in range(r):
        array.append(getline())
    
    k = int(input())
    
    recs = []
    for _ in range(k):
        recs.append(getline())
    
    dp = [[[] for _ in range(c)] for _ in range(r)]
    
    
    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if j != c-1 :
                temp = dp[i][j+1]
                v = array[i][j]
                gemp = [e+v for e in temp]
                gemp.insert(0, v)
                dp[i][j] = gemp
                
            else :
                dp[i][j].append(array[i][j])
            
    for i,j,x,y in recs:
        i-=1
        j-=1
        x-=1
        y-=1
        temp = 0
        for s in range(i, x+1):
            temp += dp[s][j][y-j]
        print(temp)
            

def solution_time_excess():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
    
    r, c = getline()
    array = []
    for _ in range(r):
        array.append(getline())
    
    k = int(input())
    
    recs = []
    for _ in range(k):
        recs.append(getline())

    for rec in recs:
        i, j, x, y = [e-1 for e in rec]
        answer = 0
        for rr in range(i, x+1):
            answer += sum([array[rr][cc] for cc in range(j, y+1)])
        
        print(answer)
       


def solution():
    import sys
    def getline():
        return list(map(int, sys.stdin.readline().rstrip().split()))
    
    r, c = getline()
    array = []
    for _ in range(r):
        array.append(getline())
    
    k = int(input())
    
    recs = []
    for _ in range(k):
        recs.append(getline())

    
    dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if j == c-1:
                dp[i][j]=array[i][j]
            else:
                dp[i][j]=dp[i][j+1]+array[i][j]
                
    for i in range(r-2, -1, -1):
        for j in range(c-1, -1, -1):            
            dp[i][j]+=dp[i+1][j]
    
    print(dp)
    for rec in recs:
        i,j,x,y = [e-1 for e in rec]
        
        answer = dp[i][j] + dp[x+1][y+1] - dp[i][y+1] - dp[x+1][j]
        print(answer)
              
       
          
solution()