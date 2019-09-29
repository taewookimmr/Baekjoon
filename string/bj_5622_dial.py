word = list(input())
word = list(map(lambda x: ord(x)-65, word))
def func(x):

    if x < 18:
        return x//3 + 3
    elif x == 18:
        return 8
    elif x <= 21 :
        return 9
    else :
        return 10

def s(x, a):
    if x >= a : return 1
    else: return 0

def v(x):
    return 3*s(x, 0) + s(x, 3) + s(x, 6) + s(x, 9) + s(x, 12) + s(x, 15) + s(x, 19) + s(x, 22)

word = list(map(v, word))
print(sum(word))
