import sys 
def main():
    n = int(input())
    triangle = []
    for _ in range(n):
        a = sys.stdin.readline().rstrip().split()
        triangle.append([int(e) for e in a])

    accum = []
    for i in range(n):
        accum = [max(a+c, b+c) for a,b,c in zip([0]+accum, accum+[0], triangle[i])]
    print(max(accum))
            


main()


