def main():
    n = int(input())

    if n <= 2:
        print((n-1)*17 - (n-2)*9)
        return 

    dp = [[1 for _ in range(10)] for _ in range(3)]
    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0


    dp[1][1] = 1 + dp[0][2]
    for i in range(2, 8+1):
        dp[1][i] = dp[0][i-1] + dp[0][i+1]
    dp[1][9] = dp[0][8]

    # dp[0] 전전
    # dp[1] 전
    # dp[2] 현재

    # 3부터 시작
    j = []
    for i in range(n-2):
        j = [i%3, (i+1)%3, (i+2)%3]
        dp[j[2]][1] = dp[j[0]][1] + dp[j[1]][2]
        for i in range(2, 8+1):
            dp[j[2]][i] = dp[j[1]][i-1] + dp[j[1]][i+1]
        dp[j[2]][9] = dp[j[1]][8]
    
    print(sum(dp[j[2]])%1000000000)

        


    

main()
    