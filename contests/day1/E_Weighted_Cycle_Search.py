from collections import defaultdict, deque


for _ in range(int(input())):
    n,k = map(int,input().split())
    inp = []
    for i in range(k):
        a,b,c=  map(int,input().split())
        inp.append([a,b,c])
    inp = sorted(inp, key = lambda x:x[2], reverse=True)
    
    parent = {i:i for i in range(n+1)}
    
    def find(node):
        if node==parent[node]:
            return node
        parent[node]=find(parent[node])
        return parent[node]
    size = [0]*(n+1)
    def union(parentX,parentY):
        if size[parentX]>size[parenY]:
            parent[parentY]=parentX
        elif size[parentX]<size[parenY]:
            parent[parentX]=parentY
        else:
            parent[parentX]=parentY
            size[parentY]+=1
            
    
    graph=defaultdict(list)
    weight=float('inf')
    start,end=1,1
    for a,b,c in inp:
        parentX=find(b)
        parenY=find(a)
        if parentX!=parenY:
            graph[a].append(b)
            graph[b].append(a)
            union(parentX,parenY)
        else:
            if c<weight:
                weight=c
                start=a
                end=b
    queue = deque()
    queue.append(start)
    visited = set({start})
    path = {start:-1}
    while queue:
        for i in range(len(queue)):
            node=queue.popleft()
            if node==end:
                queue=[]
                break
            for child in graph[node]:
                if child not in visited:
                    path[child]=node
                    queue.append(child)
                    visited.add(child)
    ele=end
    ans=[start]
    while path[ele]!=-1:
        ans.append(ele)
        ele=path[ele]
    print(weight,len(ans))
    print(*ans[::-1])
        
            
            
            
        
        
        
    
    
        
