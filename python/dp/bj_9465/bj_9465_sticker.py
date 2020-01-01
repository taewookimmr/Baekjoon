def solution():
    ntk = int(input())
    for _ in range(ntk):
        m = int(input())
        stickers =[]
        for _ in range(2):
            stickers.append(list(map(int, input().rstrip().split())))

        dp = [[0 for _ in range(3)] for _ in range(m)] 
        dp[0][0] = 0
        dp[0][1] = stickers[1][0]
        dp[0][2] = stickers[0][0]

        for c in range(1, m):
            dp[c][0] = max(dp[c-1])
            dp[c][1] = max(dp[c-1][0], dp[c-1][2]) + stickers[1][c]
            dp[c][2] = max(dp[c-1][0], dp[c-1][1]) + stickers[0][c]

        print(dp)

solution()               
