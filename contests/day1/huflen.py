
from collections import defaultdict
from heapq import *
from typing import Counter


s=input()
table=Counter(s)
freq=list(table.values())
heapify(freq)

graph=defaultdict(list)

while len(freq)>1:
    f=heappop(freq)
    s=heappop(freq)
    graph[f+s].append(f)
    graph[f+s].append(s)
    heappush(freq,f+s)
table=dict(sorted(table.items(),key=lambda x:x[1]))
print(graph)
