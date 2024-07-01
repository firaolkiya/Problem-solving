from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
count=0
s_row,s_col =map(int,input().split())
e_row,e_col = map(int,input().split())

if e_row==s_row and s_col==e_col:
    print(0)
else:
    s_row-=1
    e_row-=1

    s_col-=1
    e_col-=1
    board=[]
    for i in range(n):
        rows = list(input().rstrip())
        board.append(rows)

    queue=deque()
    queue.append((s_row,s_col,0,(0,0)))  

    directions=[(1,1),(-1,-1),(-1,1),(1,-1)]  

    inbound = lambda x,y:0<=x<n and 0<=y<n
    count=float('inf')
    moved=set({(s_row,s_col)})
    found=False
    while queue and not found:
        row,col,dis,path=queue.popleft()
        if (row,col)==(e_row,e_col):
                count=min(count,dis)
                found=True
                break
        for r,c in directions:
            new_r=row+r
            new_col=col+c
            if inbound(new_r,new_col) and (new_r,new_col,(r,c)) not in moved and board[new_r][new_col]==".":
                if (r,c)==path:
                    queue.append((new_r,new_col,dis,(r,c)))
                else:
                    queue.append((new_r,new_col,dis+1,(r,c)))
                moved.add((new_r,new_col,(r,c)))
    if not found:
        print(-1)
    else:
        print(count)
                
            