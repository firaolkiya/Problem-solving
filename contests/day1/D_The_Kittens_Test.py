from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
rep = [i for i in range(n+1)]
store=defaultdict(list)

for i in range(1,n+1):
    store[i].append(i)
size=[0]*(n+1)
def find(node):
    if rep[node]==node:
        return node
    rep[node]=find(rep[node])
    return rep[node]
finEl=[0]
def union(x,y):
    parentX = find(x)
    parentY=find(y)
    if size[parentX]>size[parentY]:
        rep[parentY]=parentX
        store[parentX].extend(store[parentY])
        finEl[0]=parentX
        del store[parentY]
    elif size[parentX]<size[parentY]:
        rep[parentX]=parentY
        store[parentY].extend(store[parentX])
        del store[parentX]
        finEl[0]=parentY
    else:
        rep[parentX]=parentY
        store[parentY].extend(store[parentX])
        finEl[0]=parentY
        size[parentY]+=1
    
        

for i in range(n-1):
    x,y = map(int,input().split())
    union(x,y)

print(*store[finEl[-1]][::-1])

