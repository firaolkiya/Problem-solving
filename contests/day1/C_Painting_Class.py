
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
color = list(map(int,input().split()))

graph = defaultdict(list)

for i in range(n-1):
    graph[nums[i]].append(i+2)

queue=deque()
queue.append((1,color[0]))

count=0

while(queue):
    node,col=queue.popleft()
    for child in graph[node]:
        if color[child-1]!=col:
            count+=1
        queue.append((child,color[child-1]))
print(count+1)