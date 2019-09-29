
n = int(input())
if n < 1 or n > 10**6 :
    print("out of bound")
    exit()

from collections import deque
buf = deque()
temp = (n, 0)
dct = {}
dct[n] = 0

while temp[0] != 1 :
    if temp[0] % 3 == 0 and temp[0]//3 not in dct:
        buf.append((temp[0]//3, temp[1]+1))
        dct[temp[0]//3] = temp[1]+1
    if temp[0] % 2 == 0 and temp[0]//2 not in dct:
        buf.append((temp[0]//2, temp[1]+1))
        dct[temp[0]//2] = temp[1]+1
    if temp[0]-1 not in dct:
        buf.append((temp[0]-1, temp[1]+1))
        dct[temp[0]-1] = temp[1]+1
    temp = buf.popleft()
  
print(temp[1])
    







    


