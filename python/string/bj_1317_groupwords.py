def is_groupword(w):
    dic = {}
    pi = -1
    for i in range(len(w)):
        if w[i] in dic.keys():
            if pi >= 0 and w[i] != w[pi]:
                return False
        else:
            dic[w[i]] = 0
        pi = i
    return True
    
def permutation_generation(n, preperm):
    if len(preperm) == 0:
        return [e for e in range(n)]
    pivot = 0
    breakcount = 0
    for i in range(n-1, 0, -1):
        if preperm[i-1] < preperm[i]:
            standard = preperm[i-1]
            min = preperm[i]
            index = i
            for j in range(n-1, i, -1):
                if standard < preperm[j] and preperm[j] < min:
                    min = preperm[j]
                    index = j
            # swap process
            preperm[i-1] = min
            preperm[index] = standard 
            pivot = i
            breakcount = 1
            break
    if breakcount == 0:
        return []
    return preperm[:pivot+1] + sorted(preperm[pivot+1:])
        

def solution():
    n = int(input())
    part = []
    for _ in range(n):
        part.append(input())
    answer = [] 
   
    previous = []
    present = permutation_generation(n, previous)
    while len(present) != 0 :
        temp = ""
        escape = 0
        for atom in present:
            temp += part[atom]
            if is_groupword(temp) != True:
                escape = 1
                break
        if escape == 0:
            answer.append(temp)
        if len(answer) > 1:
            print("-_-")
            return
        previous = present
        present = permutation_generation(n, previous)

    if len(answer) == 0:
        print('gg')
        return
    print(answer[0])


solution()











def old_solution():
    n = int(input())
    part = []
    for _ in range(n):
        part.append(input())
    import itertools
    answer = [] 
    perm = list(itertools.permutations([e for e in range(n)], n))
    for mole in perm:
        temp = ""
        escape = 0
        for atom in mole:
            temp += part[atom]
            if is_groupword(temp) != True:
                escape = 1
                break
        if escape == 0:
            answer.append(temp)
        if len(answer) > 1:
            print("-_-")
            return
    if len(answer) == 0:
        print('gg')
        return
    print(answer[0])
    
    



