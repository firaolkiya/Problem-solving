from collections import defaultdict, deque
import sys
input = sys.stdin.readline
graph = defaultdict(list)

n=int(input())

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs = list(map(int,input().split()))
index_map = {value: index for index, value in enumerate(bfs)}
def custom_sort(node):
    graph[node] = sorted(graph[node], key=lambda x: index_map.get(x, float('inf')))
    
for node in graph:
   custom_sort(node)

queue = deque([1])
visited = set({1})

ans=[1]
while queue:
    node=queue.popleft()
    for child in graph[node]:
        if child not in visited :
            ans.append(child)
            visited.add(child)
            queue.append(child)
                  
       
    
if ans!=bfs:
    print("No")
else:
    print("Yes")

    
        
