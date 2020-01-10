def solution():
    n = int(input())
    answer = 0
    for _ in range(n):
        word = [e for e in input().rstrip()]
        stack = [word.pop(0)]
        for i in range(len(word)):
            ch = word[i]
            if len(stack):
                if stack[-1] == ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        if len(stack) == 0:
            answer +=1

    print(answer)

solution()


