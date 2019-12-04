def solution(n):
    if n == 1:
        return [1]

    answer = [1]
    m = 2
    
    def reverseswap():
        t = len(answer)
        while t//2 >= 1:
            temp = answer[t-1]
            answer[t-1] = answer[t//2-1]
            answer[t//2-1] = temp 
            t //= 2
            if t == 1:
                 break
    
    def reversepop(u):
        t = answer.pop(0)
        answer.insert(0, u)
        answer.append(t)
        
    while m <= n:
        reverseswap()
        reversepop(m)
        m += 1
        
    return answer 
        

def solution2(n):
    answer = [0 for _ in range(n+1)]
    for i in range(1, n):
        j = i
        while j >1 :
            answer[j] = answer[j//2]
            j //= 2
        answer[1] = i+1
    answer[n] =1
    
    return answer[1:]
    
def main():
    for n in range(1, 10000):
        a = solution(n)
        b = solution2(n)
        c = sum([e-d for e, d in zip(a,b)])
        print(n, c)
    print("in the end")
main()