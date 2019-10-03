def permutation_generator(a):
    n = len(a)
    c = [0]*n
    A = list(a)
    yield A
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                temp = A[0]
                A[0] = A[i]
                A[i] = temp
            else:
                temp = A[c[i]]
                A[c[i]] = A[i]
                A[i] = temp
            yield A
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

def is_groupword(w):
    dic = {}
    pi = -1
    for i in range(len(w)):
        if w[i] in dic.keys():
            if pi >= 0 and w[i] != w[pi]:
                return False
        else:
            dic[w[i]] = 0
        pi = i
    return True
    
def solution():
    import sys
    n = int(sys.stdin.readline())
    part = []
    for _ in range(n):
        part.append(sys.stdin.readline())
    import itertools
    answer = [] 
    perm = permutation_generator([e for e in range(n)])
    for p in perm:
        temp = ""
        escape = 0
        for idx in p:
            temp += part[idx]
            if is_groupword(temp) != True:
                escape = 1
                break
        if escape == 0:
            answer.append(temp)
        if len(answer) > 1:
            sys.stdout.write('-_-'+'\n')
            return
    if len(answer) == 0:
        sys.stdout.write('gg'+'\n')
        return
    sys.stdout.write(answer[0]+'\n')
    
    
solution()