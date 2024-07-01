from collections import defaultdict, deque
from string import ascii_lowercase

lis=[]
n=int(input())
for _ in range(n):
    s=input()
    lis.append(s)

graph = defaultdict(list)
inDegree=defaultdict(int)

Tag=True
for i in range(1,n):
    min_leng=min(len(lis[i-1]),len(lis[i]))
    ind=0
    while ind<min_leng:
        if lis[i][ind]!=lis[i-1][ind]:
            graph[lis[i-1][ind]].append(lis[i][ind])
            inDegree[lis[i][ind]]+=1
            break
        if ind==len(lis[i])-1 and ind<len(lis[i]):
            Tag=False
        ind+=1
        
queue=deque() 
visited=set()
ans=[]
for node in graph:
    if inDegree[node]==0:
        queue.append(node)
while queue:
    node=queue.popleft()
    if node in visited:
        continue
    ans.append(node)
    for child in graph[node]:
        inDegree[child]-=1
        if inDegree[child]==0:
            queue.append(child)
    visited.add(node)   
            
            
letter=ascii_lowercase
ou=[]
if not Tag or len(ans)!=len(graph):
    print("Impossible")
else:
    for k in letter:
        if k not in ans:
            ou.append(k)
    ou.extend(ans)
    print("".join(ou))
            
            