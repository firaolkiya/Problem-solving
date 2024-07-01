from collections import defaultdict, deque


n, m =map(int,input().split())
start,end = map(int,input().split())

graph =defaultdict(set)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

stack=deque([start])
relation={start:0}
##print(graph)
moved=set({start})
while stack:
    for _ in range(len(stack)):
        node=stack.popleft()
        if node==end:
            stack=[]
            break
        for child in graph[node]:
            if child not in moved:
                moved.add(child)
                relation[child]=node
                stack.append(child)
k=end
relation[start]=0
ans=[]
tag=False
while k>0:
    ans.append(k)
    k=relation[k]
    if k>0 and k not in relation:
        tag=True
if not tag:
    print(len(ans)-1)                
    print(*ans[::-1])
else:
    print(-1)