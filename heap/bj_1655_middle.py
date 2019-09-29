def solution():
    import sys
    import heapq
    n = int(input())
    minheap=[]
    maxheap=[]
    m = []
    for i in range(1, n+1):
        m.append(int(input()))
    for i in range(len(m)):
        if i%2 == 0 :
            if i == 0 :
                heapq.heappush(maxheap, -m[i])
            else:
                if -maxheap[0] >= m[i]:
                    heapq.heappush(maxheap, -m[i])
                else : 
                    heapq.heappush(minheap, m[i])
                    heapq.heappush(maxheap, -heapq.heappop(minheap))
        else :
            if -maxheap[0] < m[i]:
                heapq.heappush(minheap, m[i])
            else:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
                heapq.heappush(maxheap, -m[i])
        print(-maxheap[0])
    

solution()
