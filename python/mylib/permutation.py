def permutation_generator(a):
    n = len(a)
    c = [0]*n
    A = list(a)
    yield A
    i = 1
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                temp = A[0]
                A[0] = A[i]
                A[i] = temp
            else:
                temp = A[c[i]]
                A[c[i]] = A[i]
                A[i] = temp
            yield A
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

def test():
    for i in (permutation_generator([1,2,3,4])):
        print(i)

def permutation_generation(n, preperm):
    pivot = 0
    breakcount = 0
    for i in range(n-1, 0, -1):
        if preperm[i-1] < preperm[i]:
            standard = preperm[i-1]
            minim = preperm[i]
            index = i
            for j in range(n-1, i, -1):
                if standard < preperm[j] and preperm[j] < minim:
                    minim = preperm[j]
                    index = j
            # swap process
            preperm[i-1] = minim
            preperm[index] = standard 
            pivot = i
            breakcount = 1
            break
    if breakcount == 0:
        return []
    return preperm[:pivot] + sorted(preperm[pivot:])
        

def solution():
    n = 3
    preperm = [1,0,3]
    preperm.sort()
    while len(preperm):
        preperm = permutation_generation(n, preperm)
        print(preperm)
   

solution()