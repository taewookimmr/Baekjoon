def solution():
    A,B = input().rstrip().split()
    answer = []
    for i in range(len(B)-len(A)+1):
        answer.append(sum([1 if a != b else 0 for a,b in zip(A,B[i:i+len(A)])]))
    print(min(answer))

solution()