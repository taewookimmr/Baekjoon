def solution():
    import sys
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        data = int(sys.stdin.readline().rstrip())
        queue = []
        count = 0
        queue.append(data)
        while len(queue):
            t = queue.pop(0)
            if t > 0 :
                queue.append(t-1)
                queue.append(t-2)
                queue.append(t-3)
            elif t == 0 :
                count += 1
        
        print(count)
                
def solution1() :
    n = int(input())
    for _ in range(n):
        m = int(input())
        dic = {}
        dic[1] = 1
        dic[2] = 2
        dic[3] = 4
        for i in range(4, n+1):
            dic[i] = dic[i-1] + dic[i-2] + dic[i-3]
        
        print(dic[n])
        
solution()