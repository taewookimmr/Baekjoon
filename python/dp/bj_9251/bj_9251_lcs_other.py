def solution():
    A = [e for e in input().rstrip()]
    B = [e for e in input().rstrip()]
    la = len(A)
    lb = len(B)

    dp = [[0 for _ in range(lb+1)] for _ in range(la+1)]
    for i in range(1,la+1):
        for j in range(1,lb+1):
            if A[i-1]==B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[la][lb])

solution()