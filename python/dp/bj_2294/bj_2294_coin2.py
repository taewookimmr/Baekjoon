def solution_bfs_memory_excess():
    import sys
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    
    queue = [[0,0]]

    while len(queue):
        acc, depth = queue.pop(0)
        for c in coin :
            if acc + c < k :
                queue.append([acc+c, depth+1])
            if acc + c == k:
                print(depth+1)
                return


def solution():
    import sys
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    coin = []
    for _ in range(n):
        coin.append(int(input()))   
    coin.sort()
    INF = 100000
    dp = [INF for _ in range(k+1)]
    dp[0]=0
    # dp[k]를 구하는 것이 목표
    # dp[j] = dp[j-coin[i]] + 1, 이런식으로 가야하나? min을 사용해야지 
    for i in range(n):
        for j in range(1,k+1):
            if j - coin[i] >= 0:
                dp[j] = min(dp[j], dp[j-coin[i]]+1)

    if dp[k] == INF:
        print(-1)
    else:
        print(dp[k])
solution()
        