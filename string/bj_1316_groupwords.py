n = int(input())
count = 0
for i in range(n):
    w = input()
    dic = {}
    pi = -1
    for i in range(len(w)):
        if w[i] in dic.keys():
            if pi >= 0 and w[i] != w[pi]:
                count -= 1
                break
        else:
            dic[w[i]] = 0
        pi = i
    count += 1

print(count)


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
    