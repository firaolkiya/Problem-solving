
from collections import defaultdict, deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n=int(input())
    graph=defaultdict()
    s=input()
    for i in range(n):
        left,right= map(int,input().split(" "))
        graph[i+1]=[left,right]
    
    
    queue = deque([(1,0)])
    count=n
    while queue:
        node,cur = queue.popleft()
        if graph[node][1]==0 and graph[node][0]==0:
            count=min(count,cur)
        elif graph[node][1]==0:
            cur+=int(s[node-1]!="L")
            queue.append((graph[node][0],cur))
        elif graph[node][0]==0:
            cur+=int(s[node-1]!="R")
            queue.append((graph[node][1],cur))
        else:
            m=cur+int(s[node-1]!="R")
            queue.append((graph[node][1],m))
            
            cur+=int(s[node-1]!="L")
            queue.append((graph[node][0],cur))
        
    print(count)
            
        
            
    