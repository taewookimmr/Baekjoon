def solution():
    import heapq
    import sys
    heap = [] 
    n = int(input())
    for _ in range(n):
        m = int(sys.stdin.readline().rstrip())
        if m != 0:
            heapq.heappush(heap, [abs(m), m])
        else:
            if len(heap) != 0:
                a, b = heapq.heappop(heap)
                print(b)
            else:
                print(0)

solution()