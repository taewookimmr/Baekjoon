word = list(input())
dic = {}
for i in range(26):
    dic[chr(i+97)] = 0
for w in word:
    dic[w] += 1
for key in dic :
    print(dic[key], end = ' ')


def good_solution():
    word = input()
    for i in range(97, 97+26):
        print(word.count(chr(i)), end = ' ')