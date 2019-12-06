def solution():
    import sys 
    n = int(input())
    schedule = []
    for _ in range(n):
        time, earn = list(map(int, sys.stdin.readline().rstrip().split()))
        schedule.append([time, earn])
    schedule.append([0,0])
    dp = [0 for _ in range(n+1)]
    for i in range(n+1):
        for j in range(i+1):
            past = j 
            future = past + schedule[past][0]
            if future <= i :
                dp[i] = max(max(dp), dp[past]+schedule[past][1]) 
    print(max(dp))
                


solution()
