def solution():
    dic = [{},{}]
    answer =0
    for i in range(2):
        for e in input().rstrip():
            dic[i][e] = dic[i].get(e, 0) +1
            answer +=1 ## 두 단어의 길이가 저장된다. 현재 2중 반복문을 나가면.
    for i in dic[0].keys():
        for j in dic[1].keys():
            if i == j:
                answer -= min(dic[0][i], dic[1][j])*2
    print(answer)

def solution_other():
    s1 = input()
    s2 = input()
    ans = 0
    a, b = [0]*26, [0]*26
    for i in range(len(s1)):
        a[ord(s1[i])-97] += 1
    for i in range(len(s2)):
        b[ord(s2[i])-97] += 1
    for i in range(26):
        ans += abs(a[i]-b[i])
    print(ans)


solution()