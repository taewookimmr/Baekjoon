import sys
a,b = sys.stdin.readline().split()
def func(l):
    l = list(l)
    l.reverse()
    l = "".join(l)
    l = int(l)
    return l
a1 = func(a)
b1 = func(b)
if a1 > b1:
    print(a1)
else: 
    print(b1)

print(max(input()[::-1].split()))