
from collections import defaultdict, deque
from heapq import *


n,k = map(int,input().split())
graph=defaultdict(list)
inDegree=[0]*n
for _ in range(k):
    a,b = map(int,input().split())
    graph[a].append(b)
    inDegree[b-1]+=1


queue=[]
ans=[]
for i in range(n):
    if inDegree[i]==0:
        heappush(queue,i+1)
        
while queue:
        
    node=heappop(queue)
    ans.append(node)
    for child in graph[node]:
        inDegree[child-1]-=1
        if inDegree[child-1]==0:
            heappush(queue,child)
                
if len(ans)==n:
    print(*ans)
else:
    print(-1)
