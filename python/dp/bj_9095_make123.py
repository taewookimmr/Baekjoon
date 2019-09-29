# 정수 n
# 정수 n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그램 작성
# when n = 3
# >> 1+1+1, 1+2, 

m = int(input())

for _ in range(m):
    n = int(input())
    dic = {}
    dic[1] = 1
    dic[2] = 2
    dic[3] = 4

    for i in range(4, n+1):
        dic[i] = dic[i-1] + dic[i-2] + dic[i-3]

    print(dic[n])