import sys
word = list(input())
for i in range(26):
    w = chr(i+97)
    if w in word:
        print(word.index(w), end = ' ')
    else:
        print(-1, end= ' ')

