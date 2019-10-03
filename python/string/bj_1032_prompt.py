n = int(input())
words = []
for _ in range(n):
    words.append(input())

m = len(words[0])
answer = list(words[0])
for i in range(m):
    for j in range(1, n):
        if answer[i] != words[j][i]:
            answer[i] = '?'
    
print(''.join(answer))
