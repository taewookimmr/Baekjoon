def solution():
    import sys
    R,G,B = 0, 0, 0
    for i in range(int(sys.stdin.readline())):
        r, g, b = map(int, sys.stdin.readline().rstrip().split())
        r += min(G, B)
        g += min(R, B)
        b += min(R, G)
        R,G,B = r,g,b
    print(min(R,G,B))
        