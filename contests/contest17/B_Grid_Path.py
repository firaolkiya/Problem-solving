import sys
input = sys.stdin.readline

def solve(n,m):
    board = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            up=left=float('inf')
            if j>0:
                left=board[i][j-1]+i+1
            if up>0:
                up=board[i-1][j]+j+1
            board[i][j]=min(left,up)
    return board[-1][-1]
    

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    if k==solve(n,m):
        print("YES")
    else:
        print("NO")
    