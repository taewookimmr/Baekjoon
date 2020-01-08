def solution():
    src = input().rstrip()
    n = len(src)
    a, b= 0,0
    for i in range(n-2):
        if src[i:i+3] == "JOI":
            a+=1
        if src[i:i+3] == "IOI":
            b+=1
    print(a)
    print(b)



solution()