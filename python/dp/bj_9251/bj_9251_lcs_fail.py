def solution():
    def getLine():
        import sys
        temp = sys.stdin.readline().rstrip()
        result = []
        for e in temp:
            result.append(e)
        return result 

    a = getLine()
    b = getLine()
    src = ""
    target = ""
    if len(a) < len(b) :
        src = a
        target = b
    else:
        src = b
        target = a

    answer = []
    dic = {}

    def recur(parent, target):

        def matching(parent, target):
            _p = parent[:]
            _t = target[:]
            for e in _t:
                if e == _p[0]:
                    _p.pop(0)
                    if len(_p) == 0:
                         return True
            return False

        def popones(parent):
            n = len(parent)
            temp = []
            for i in range(n):
                gemp = parent[:]
                gemp.pop(i)
                temp.append(gemp)
            return temp
      
        if matching(parent, target):
            answer.append(len(parent))
            return 
        else:
            dic["".join(parent)] = -1
            for child in popones(parent):
                if "".join(child) not in dic.keys():
                    recur(child, target)

    recur(src, target)
    print(max(answer))

solution()
