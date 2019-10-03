import sys
from queue import PriorityQueue
 
n, k = list(map(int, sys.stdin.readline().split()))
 
jew = []
bag = []
for i in range(n):
    jew.append(list(map(int, sys.stdin.readline().split())))
for i in range(k):
    bag.append(int(sys.stdin.readline()))
jew.sort(key = lambda item: item[1], reverse = True) 
for i in range(n):
    jew[i].insert(0, i) 

 
jew.sort(key = lambda item: item[1])  
bag.sort() 
q = PriorityQueue()
 
idx = 0
sum = 0
for i in range(k):  
    while (idx < n and bag[i] >= jew[idx][1]):  
        q.put((jew[idx][0], jew[idx][2]))
 
        idx += 1
    if not q.empty():
       sum += q.get()[1]
print(sum)
