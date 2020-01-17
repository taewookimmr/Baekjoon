def solution():
    n, k = list(map(lambda x: int(x), input().rstrip().split(" ")))
    word = []
    visited = [False for _ in range(26)]
    for i in list(map(lambda x:ord(x)-ord('a'), ['a', 'c', 'i', 'n', 't'])):
        visited[i] = True
    answer = [0]

    def howMany(alpha, cnt, n, k):
        if cnt == k : 
            temp = 0
            for i in range(n):
                flag = True
                for j in range(len(word[i])):
                    node = ord(word[i][j]) - ord('a')
                    if not visited[node]:
                        flag = False
                        break
                if flag:
                    temp +=1
            answer[0] = max(answer[0], temp)
            return
        
        for i in range(alpha, 26):
            if not visited[i]:
                visited[i] = True
                howMany(i, cnt+1, n,k)
                visited[i] = False


    if k<5:
        print(0)
        return
    elif(k == 26):
        print(n)
        return
    
    k-=5
    for i in range(n):
        word.append(input().rstrip()[4:][:-4])

    howMany(0,0,n,k)
    print(answer[0])

solution()