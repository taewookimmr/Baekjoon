# 규칙
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다,
# 연속된 세 개의 계단을 모두 밟아서는 안된다. 시작 점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다. 

m = int(input())

reward = [0] * m

for i in range(m):
    reward[i] = int(input())
    

Q = [0] * m
Q[0] = reward[0]
Q[1] = reward[0] + reward[1]
Q[2] = max([reward[1] + reward[2], reward[0] + reward[2]])


for i in range(3, m):
    way1 = Q[i-3] + reward[i-1] + reward[i]
    way2 = Q[i-2] + reward[i]
    Q[i] = max(way1, way2)
    
print(Q[m-1])


    
    


  
