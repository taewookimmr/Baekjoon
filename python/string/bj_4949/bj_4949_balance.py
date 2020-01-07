def solution():
    while True:
        mystr = [ch for ch in input().rstrip()]
        if len(mystr) == 1 and mystr[0]=='.' : break
        stack = []
        while len(mystr):
            ch = mystr.pop(0)
            if ch in ["(", "["]:
                stack.append(ch)
            elif ch == ")":
                if stack[-1] != "(":
                    print("no")
                    break
                else :
                    stack.pop()
            elif ch == "]":
                if stack[-1] != "[":
                    print("no")
                    break
                else:
                    stack.pop()
        else:
            if len(stack):
                print("no")
            else:
                print("yes") 
solution()

