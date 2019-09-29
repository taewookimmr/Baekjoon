import sys
chess =[]
count =0 
for i in range(8):
    if i%2 == 0:
        for idx, w in enumerate(sys.stdin.readline()):
            if idx%2 == 0 and w == 'F':
                count += 1
    else :
          for idx, w in enumerate(sys.stdin.readline()):
            if idx%2 != 0 and w == 'F':
                count += 1

print(count)

testlist = [1,2,3,4]
print(testlist[::2])
