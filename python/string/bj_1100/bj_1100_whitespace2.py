def solution():
    answer = 0
    for i in range(8):
      a = input().rstrip()
      for j, e in enumerate(a):
            if e == 'F' and i%2 == j%2 :
                answer +=1
    print(answer) 

solution()