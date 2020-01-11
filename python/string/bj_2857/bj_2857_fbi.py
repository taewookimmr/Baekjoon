def solution():
    answer =[]
    for i in range(5):
        if input().rstrip().count('FBI'):
            answer.append(i+1)
    if len(answer):
        print(" ".join([str(e) for e in answer]))
    else:
        print("HE GOT AWAY!")

solution()