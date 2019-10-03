check =["c=", "c-","dz=","d-","lj","nj","s=","z="]
word = input()
s = 0
for c in check:
    s += word.count(c)

print(len(word)-s)
