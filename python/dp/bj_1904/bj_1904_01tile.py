def solution():
    n = int(input())
    if n<=2 : 
        print(n)
        return 

    a,b,c,=1,2,0
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    print(c%15746)

def solution2():
    import math
    a= math.sqrt(5)
    n = int(input())
    if n<=2 : 
        print(n)
        return
    b = ((1+a)/2)**n
    c = ((1-a)/2)**n
    d = (5+a)/10
    e = (5-a)/10
    print(int(d*b+e*c))

solution2()