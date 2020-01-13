def solution():
    n = int(input())
    tank=[input().rstrip()]
    for _ in range(n):
        temp = input().rstrip()
        if  len(temp)%2 and (temp[::-1] in tank or temp==temp[::-1]):
            print(len(temp), temp[len(temp)//2])
        else:
            tank.append(temp)
solution()