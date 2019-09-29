import sys
n = int(sys.stdin.readline().rstrip())
if n<=1000:
    memo = [[] for i in range(n)]
    for i in range(n):
        if i == 0:
            rgb = list(map(int, sys.stdin.readline().rstrip().split()))
            length = len(rgb)
            for j in range(length):
                memo[0].append(rgb[j])
        else :
            rgb = list(map(int, sys.stdin.readline().rstrip().split()))
            length = len(rgb)
            for j in range(length):
                if j==0:
                    memo[i].append(rgb[j]+min(memo[i-1][1],memo[i-1][2]))
                if j == 1:
                    memo[i].append(rgb[j] + min(memo[i-1][0],memo[i-1][2]))
                if j == 2:
                    memo[i].append(rgb[j] + min(memo[i-1][0],memo[i-1][1]))
    print(min(memo[n-1]))
