def solution_simple():
    dp = [0]*(int(input())+1) 
    packs = list(map(int, input().rstrip().split()))

    for i in range(n, -1, -1):
        for j, p in enumerate(packs):
            if i-(j+1) >= 0:
                dp[i-(j+1)] = max(dp[i-(j+1)], dp[i] + p)
                
    print(int(dp[0]))
   

def solution_1st_trial():
    n = int(input())
    packs = list(map(int, input().rstrip().split()))
    packs.insert(0, 0) # dummy for indexing
    unitPrices = [[e/i,i] for i, e in enumerate(packs) if i]
    unitPrices.sort(reverse=True)

    dp = [0]*(n+1) 
    dp[n] = 0
    # dp[남은 개수] = 최대 금액     
    # #목적은 dp[0]을 구하는 것

    for i in range(n, -1, -1):
        for up, j in unitPrices:
            if i-j >= 0:
                dp[i-j] = max(dp[i-j], dp[i] + up*j)
                
    print(int(dp[0]))

solution_simple()