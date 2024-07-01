
from collections import defaultdict, deque


tree  =defaultdict(list)
for _ in range(int(input())-1):
    a,b = map(int,input().split())
    tree[b].append(a)
    tree[a].append(b)
    
init = list(map(int,input().split()))
target = list(map(int,input().split()))


queue = deque()
queue.append((0,0,1,0))
total_count=[]

visited=set()
while queue:
    even,odd,node,level = queue.popleft()
    flapped=[even,odd]
    if (level%2==1 and odd%2==1 )or (level%2==0 and even%2==1):
        init[node-1]=0 if init[node-1]==1 else 1
    if init[node-1]!=target[node-1]:
        total_count.append(node)
        flapped[level%2]+=1
    for child in tree[node]:
        if child not in visited:
            visited.add(child)
            queue.append((flapped[0],flapped[1],child,level+1))
print(len(total_count))
for k in total_count:
    print(k)

        
    