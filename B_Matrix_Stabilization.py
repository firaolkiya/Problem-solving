import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    inbound = lambda x,y:0<=x<n and 0<=y<m
    mat = []
    for i in range(n):
        lis =list(map(int,input().split()))
        mat.append(lis[::])
    for i in range(n):
        for j in range(m):
            right =  mat[i][j+1] if inbound(i,j+1)  else 0
            down =  mat[i+1][j] if inbound(i+1,j)  else 0
            left =  mat[i][j-1] if inbound(i,j-1)  else 0
            up =  mat[i-1][j] if inbound(i-1,j)  else 0
            
            mat[i][j]=min(mat[i][j],max(right,down,up,left))
    for mt in mat:
        print(*mt)