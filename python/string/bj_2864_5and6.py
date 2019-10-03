def solution():
    import sys
    answer = []
    a, b = sys.stdin.readline().split()
    a= a.replace('6', '5')
    b= b.replace('6', '5')
    answer.append(int(a) + int(b))
    a= a.replace('5', '6')
    b =b.replace('5', '6')
    answer.append(int(a) + int(b))
    for a in answer :
        print(a, end = ' ')


def short_solution():
    s=input()
    def r(a,b):
        return eval(s.replace(a,b).replace(' ', '+'))
    print("{} {}".format(r('6', '5'), r('5', '6')))

short_solution()