def solution():
    word = input()
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n-1-i]:
            print(0)
            return
    print(1)
solution()

def short_solution():
    s=input()
    print(int(s==s[::-1]))
