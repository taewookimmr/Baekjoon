def solution():
    import heapq
    import sys
    heap = [] 
    n = int(input())
    for _ in range(n):
        m = int(sys.stdin.readline().rstrip())
        if m != 0:
            heapq.heappush(heap, -m)
        else:
            if len(heap) != 0:
                print(-heapq.heappop(heap))
            else:
                print(0)

solution()