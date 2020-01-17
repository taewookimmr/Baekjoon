def solution():
    emoji = [":-)", ":-("]
    src = input().rstrip()
    answer = []
    for emo in emoji:
        answer.append(src.count(emo))
    
    if sum(answer):
        if answer[0]==answer[1]:
            print("unsure")
        else:
            if answer[0] > answer[1]:
                print("happy")
            else:
                print("sad")
    else:
        print("none")




solution()