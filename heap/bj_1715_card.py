import heapq

def solution():
    n = int(input())

    if n == 1:
        print(0)
        return
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(input()))

    sum = 0
    while len(heap) != 0 :
        a= heapq.heappop(heap) + heapq.heappop(heap)
        sum += a
        if len(heap) == 0 :
            break
        heapq.heappush(heap, a)
   
    print(sum)

solution()
