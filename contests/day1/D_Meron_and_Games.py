from collections import Counter
from heapq import *


m=  int(input())
nums=list(map(int,input().split()))
k=Counter(nums)
notdel=set()
heap=[[-i*k[i],i] for i in k]
heapify(heap)


ans=0

while heap:
    large=heappop(heap)
    if large[1] in notdel:
        continue
    notdel.add(large[1]+1)
    notdel.add(large[1]-1)
  
    ans-=large[0]
   
print(ans)