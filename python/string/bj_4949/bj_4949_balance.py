def solution():
    ## 너무 생각없이 짰네,,,너무 길다..지저분스,,간단하게 만들자
    while True:
        mystr = [ch for ch in input().rstrip()]
        if len(mystr) == 1 and mystr[0]=='.' : break
        stack = []
        while len(mystr):
            ch = mystr.pop(0)
            if ch in ["(", "["]:
                stack.append(ch)
            elif ch == ")":
                if len(stack):
                    if stack[-1] != "(":
                        print("no")
                        break
                    else :
                        stack.pop()
                else:
                    print("no")
                    break
            elif ch == "]":
                if len(stack):
                    if stack[-1] != "[":
                        print("no")
                        break
                    else:
                        stack.pop()
                else:
                    print("no")
                    break
        else:
            if len(stack):
                print("no")
            else:
                print("yes") 

def solution_other():
    check ='([])'
    while True:
        src = input().rstrip()
        if src == ".\n": break
        temp = []
        for ch in src:
            if ch in check:
                if ch == ')' and len(temp) > 0 and temp[-1] == "(":
                    temp.pop()
                elif ch == ']' and len(temp) > 0 and temp[-1] == "[":
                    temp.pop()
                else:
                    temp.append(ch)
        print('yes' if no temp else 'no')
  
solution()

