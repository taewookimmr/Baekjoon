   
import sys
def old_solution():
    word = input()
    bomb = input()

    while bomb in word:
        word = "".join(word.split(bomb))

    if word == "":
        print("FRULA")
    else:
        print(word)


def solution():
    word = input()
    bomb = input()
    
    n = len(word)
    blen = len(bomb)
    
    check = []
    clen = 0
    i = 0
    while i < n:
        check.append(word[i])
        clen += 1
        i+=1
        if clen >= blen:
            for j in range(-1, -blen-1, -1):
                if check[j] != bomb[j]:
                    break
            else : 
                a = 0
                while a < blen:
                    check.pop()
                    clen -=1
                    a+=1

    print(''.join(check) if clen != 0 else 'FRULA')


solution()