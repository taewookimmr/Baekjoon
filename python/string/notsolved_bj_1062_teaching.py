import sys
from itertools import combinations


def solution():
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    words = []
    u = set()
    for _ in range(n):
       s = set(sys.stdin.readline().rstrip())
       u = u | s
       words.append(list(s))
    u = list(u)

    answer = []
    for combi in combinations(u, m):
        maxim = 0 
        for word in words:
            for w in word:
                if w not in combi:
                    break
            else :
                maxim += 1
                if maxim == n :
                    print(n)
        answer.append(maxim)
    print(max(answer))

        
solution()
    