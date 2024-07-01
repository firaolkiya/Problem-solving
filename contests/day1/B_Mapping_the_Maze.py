from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
 
graph = defaultdict(set)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
counter = defaultdict(int)
for node in graph:
    counter[len(graph[node])]+=1
if counter[2]==n:
    print("ring topology")
elif counter[1]==n-1 and counter[n-1]==1:
    print("star topology")
elif counter[1]==2 and counter[2]==n-2:
    print("bus topology")
else:
    print("unknown topology")
