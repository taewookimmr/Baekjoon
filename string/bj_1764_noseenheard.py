import sys
n,m = list(map(int, sys.stdin.readline().split()))
unseen = [input() for _ in range(n)]
unheard = [input() for _ in range(m)]
uni = list(set(unseen) & set(unheard)) 
print(len(uni))
for e in sorted(uni):
    print(e)