def solution():
    n = int(input())
    if n <= 10:
        return n
    def check(m):
        tail = m%10
        while m :
            m = m//10
            if m:
                nexttail = m%10
                if nexttail <= tail:
                    return False
                tail = nexttail
        return True
        
solution()
    