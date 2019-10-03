import sys
a,b = sys.stdin.readline().split()

delta = len(b)-len(a)
if delta == 0 :
    print( sum([1 if ord(i) - ord(j) != 0 else 0 for i, j in zip(a,b)]) )
else :
    answer = []
    for i in range(0, delta+1):
        answer.append(sum([1 if ord(i) - ord(j) != 0 else 0 for i, j in zip(a, b[i:i+ len(a)])]))
    print (min(answer))


def solution():
    import sys
    a,b = sys.stdin.readline().split()
    c = len(b)-len(a)+1
    print(min( [sum([1 if i != j else 0 for i, j in zip(a, b[i:i+ len(a)])]) for i in range(c)]))


    