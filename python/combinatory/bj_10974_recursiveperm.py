def solution():
    n = int(input())
    from itertools import permutations
    for e in permutations(range(1,n+1), n):
        for i in e:
            print(i, end= ' ')
        print('')


def other_solution():
    n = int(input())
    arr, visit = [], [False for _ in range(n)]
    
    def recursive():
        if len(arr) == n:
            for i in arr:
                print(i + 1, end = " ")
            print()
        
        for i in range(n):
            if visit[i] != True:
                visit[i] = True
                arr.append(i)
                recursive()
                visit[i] = False
                arr.pop()
    recursive()


other_solution()
