import sys
input = sys.stdin.readline

n = int(input())
nums= list(map(int,input().split()))
degree = [0]*(n+1)
rep = {i:i for i in range(1,n+1)}

def find(node):
    if rep[node]==node:
        return node
    rep[node]=find(rep[node])
    return rep[node]
def union(x,y):
    parentX = find(x)
    parentY=find(y)
    if degree[parentX]>degree[parentY]:
        rep[parentY]=parentX
    elif degree[parentX]<degree[parentY]:
        rep[parentX]=parentY
    else:
        degree[parentY]+=1
        rep[parentX]=parentY



for i in range(n):
    union(i+1,nums[i])
ans=set()
for i in range(1,n+1):
    ans.add(find(i))
print(len(ans))