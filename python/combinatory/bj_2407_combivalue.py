import sys
n, m = list(map(int, sys.stdin.readline().rstrip().split()))

def custom_combination(n, k):
    num = 1
    den = 1
    k = min(n-k, k)
    for i in range(1, k+1):
        den *= i
        num *= n+1-i
    return num//den

print(custom_combination(n,m))

def other_solution():
    import math
    n,r = map(int, input().split())
    f = math.factorial
    print(f(n)//(f(r)*f(n-r)))