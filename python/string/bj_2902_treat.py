longword = input()
answer = [longword[0]]
while longword.find('-') != -1 :
    pos = longword.find('-')
    longword = longword[pos+1:]
    answer.append(longword[0])
print("".join(answer))

def solution():
    for i in input().split('-'):  print(i[0], end='')
   
