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




solution()
    