
def solution_bfs():
    import sys
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    
    answer = 0
    queue = [[0,0]]
    while len(queue):
        accum, prev = queue.pop(0)
        if accum == k :
            answer +=1
        elif accum > k :
            continue
        
        for v in coin:
            if accum < k and prev <= v:
                queue.append([accum+v, v])
    print(answer)
 
 

def solution():
    import sys
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in range(n):
        for j in range(1, k+1):
            if j >= coin[i]:
                dp[j] += dp[j-coin[i]]
                
    print(dp[k])

        
solution()
        
        