def solution():
    A = [e for e in input().rstrip()]
    B = [e for e in input().rstrip()]
    n = len(A)

    dic = {}
    for i in range(1, 1+2**n):
        perm = []
        for j in range(n):
            if (1<<j)&i:
                perm.append(j)
        src = [A[e] for e in perm]

        dst =[] 
        if len(src):
            for k, e in enumerate(B):
                if e == src[0]:
                    src.pop(0)
                    dst.append(k)
                    if len(src) == 0:
                        break

            if len(src) == 0 :
                dic["".join([str(e) for e in perm])] = dst
        
    print(dic)

solution()