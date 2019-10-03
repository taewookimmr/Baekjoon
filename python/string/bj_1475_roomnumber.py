from collections import Counter 

def mapping(x):
    if x == '6': return '9'
    else : return '6'

roomnum = list(input())

state = {}
numlist = [str(e) for e in range(10)]
for n in numlist:
    state[n] = 1

count =  1
for num in roomnum:
    if state[num]== 0:
        if  num != '6' and num != '9':
            count += 1
            for n in numlist:
                state[n] += 1
        else :
            if state[mapping(num)] == 0:
                count += 1
                for n in numlist:
                    state[n] += 1


    if num != '6' and num != '9':
        state[num] -= 1
    else :
        if state[num] != 0:
             state[num]-=1
        else :
            if state[mapping(num)] != 0:
                state[mapping(num)] -= 1
   

print(count)            


def good_solution():
    a=input()
    b=list()
    for i in range(10):
        b.append(a.count(str(i)))
    if (b[6]+b[9])%2==0:
        b[6]=(b[6]+b[9])//2
    else:
        b[6]=(b[6]+b[9])//2+1
    del b[9]
    print(max(b))

                
