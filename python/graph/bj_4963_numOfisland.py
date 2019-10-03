def solution():
    import sys 
    sys.setrecursionlimit(100000)
    while True:
        w, h = list(map(int, sys.stdin.readline().rstrip().split()))
        if w == 0 and h == 0:
            return
        else : 
            land = []
            for r in range(h):
                c = list(map(int, sys.stdin.readline().rstrip().split()))
                for i in range(len(c)):
                    if c[i] == 1:
                        land.append([r, i])
            count = 0
            while(len(land)):
                count += 1
                r, c = land.pop()
                def recursive(rr, cc):
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if [rr+i, cc+j] in land:
                                land.remove([rr+i, cc+j]) 
                                recursive(rr+i, cc+j)        
                recursive(r, c)
        print(count)
                
def solution2():
    import sys
    sys.setrecursionlimit(10**6)
    

            
    while True:
        w,h = map(int, input().split())
        if w and h:
            c = 0
            board = []
            for _ in range(h):
                board.append(list(map(int, input().split())))
                
            def island(x,y):
                if x<0 or y<0 or x>=h or y>=w:
                    return
                if board[x][y] == 1:
                    board[x][y] = 0
                    island(x-1,y-1)
                    island(x,y-1)
                    island(x+1,y-1)
                    island(x-1,y)
                    island(x+1,y)
                    island(x-1,y+1)
                    island(x,y+1)
                    island(x+1,y+1) 
                        
            for i in range(h):
                for j in range(w):
                    if board[i][j] == 1:
                        c += 1
                        island(i,j)
            print(c)
        else:
            break

                                     
            
                    
                    
                          
                

solution()
