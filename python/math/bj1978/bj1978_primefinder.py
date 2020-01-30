def solution():
    def isPrime(n): 
        import math
        for e in range(2, int(math.sqrt(n))+1):
            if n%e == 0 : return False
        return True
    _ = input()
    print(sum([1 if isPrime(e) else 0 for e in list(map(int, input().split()))]))    

solution()