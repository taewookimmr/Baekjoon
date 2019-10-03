def solution():
    word = input()
    print("\n".join(sorted([word[i:] for i in range(len(word))])))

solution()