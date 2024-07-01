from collections import defaultdict, deque


for _ in range(int(input())):
    n,k = map(int,input().split())
    
    inDegree = [0]*(n+1)
    graph=defaultdict(list)
    
    container=[]
    
    for _ in range(k):
        a,b,c= map(int,input().split())
        container.append((a,b,c))
        if a==0:
            graph[b].append(c)
            graph[c].append(b)
        else:
            graph[b].append(c)
            inDegree[c]+=1
    queue=deque()
    ans=[]
    for i in range(1,n+1):
        if inDegree[i]==0:
            queue.append(i)
            ans.append(i)
    color=[0]*(n+1)
    while queue:
        node= queue.popleft()
        for child in graph[node]:
            if inDegree[child]>=1:
                inDegree[child]-=1
                if inDegree[child]==0:
                    ans.append(child)
                    queue.append(child)
    index={ans[i]:i for i in range(len(ans))}
    if len(ans)!=n:
        print("NO")
    else:
        print("YES")
        for x,y,z in container:
            if x==1 or index[y]<index[z]:
                print(z,y)
            else:
                print(y,z)
        
            
        