from collections import defaultdict, deque


n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=set()
cicles = 0
for source in range(1,n+1):  #
    if source in visited:   
        continue
    moved=set()   
    node = source
    while node not in moved:
        visited.add(node)
        if len(graph[node])!=2:
            break
        moved.add(node)
        if graph[node][1] not in moved:
            node=graph[node][1]
        else:
            node=graph[node][0]
        if node in moved:
            if len(moved)>2:
                cicles+=1
            break
        
print(cicles)
            

    
    