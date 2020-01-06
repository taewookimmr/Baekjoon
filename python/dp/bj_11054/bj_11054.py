def solution():
    n = int(input())
    src = list(map(int, input().rstrip().split()))
    dp = [[1,1] for _ in range(n)]
    for i in range(0, n-1):
        for j in range(i+1, n):
            if src[i] < src[j]:
                dp[j][0] = max(dp[j][0],dp[i][0]+1)
            if src[n-1-i] < src[n-1-j]:
                dp[n-1-j][1] = max(dp[n-1-j][1], dp[n-1-i][1] + 1)
    answer = max([a+b for a,b in dp])-1
    print(answer)
solution()