from collections import defaultdict, deque
import sys
input = sys.stdin.readline

city, rail = map(int,input().split())
graph = defaultdict(list)
for i in range(rail):
    a,b = map(int,input().split())
    graph[a]=b
    graph[b]=a

bus = defaultdict(list)
for node in graph:
    for k in range(1,city+1):
        if k not in graph[node]:
            bus[node].append(k)

railway= deque([1,0])
busway = deque([1,0])
railway_di=0
visited_by_rail = set({1})
while railway:
    node,distance=  railway.popleft()
    for way in graph[node]:
        if way==city:
            railway=[]
            railway_di=distance+1
            break
        if way not in visited_by_rail:
            railway.append(way)
            visited_by_rail.add(way)
bus_way_di=0
distance=0
visited_by_bus = set({1})
while busway:
    node,distance=  busway.popleft()
    for way in bus[node]:
        if way==city:
            busway=[]
            bus_way_di=distance+1
            break
        if way not in visited_by_bus:
            busway.append(way)
            visited_by_bus.add(way)
print(max(bus_way_di,railway_di))       
    
    
