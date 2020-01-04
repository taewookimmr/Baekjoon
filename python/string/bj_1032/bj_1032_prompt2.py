def solution():
    n = int(input())
    words=[]
    for _ in range(n):
        words.append(input().rstrip())
    result = []
    for t in list(zip(*words)):
        if len(set(t)) == 1:
            result.append(t[0])
        else:
            result.append('?')
    print("".join(result))

def solution_id_2014136054():
    n = int(input())
    a = list(input())
    a_len = len(a)
    for i in range(n - 1):
        b = list(input())
        for j in range(a_len):
            if a[j] != b[j]:
                a[j] = '?'

    print(''.join(a))


solution()
    