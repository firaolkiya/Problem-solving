from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
for i in range(n-1):
    a,b,dis = map(int,input().split())
    graph[a].append((b,dis))
    graph[b].append((a,dis))

queue = deque()
queue.append((0,0))

visited=set({0})
max_d=0
while queue:
    node,dis= queue.popleft()
    max_d=max(dis,max_d)
    for child in graph[node]:
        if child[0] not in visited:
            visited.add(child[0])
            queue.append((child[0],dis+child[1]))
print(max_d)
    