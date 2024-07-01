from heapq import *

n,k,query = map(int,input().split())
nums=list(map(int,input().split()))
heap=[]

for _ in range(query):
    a,b = map(int,input().split())
    b-=1
    if a==1:
        if len(heap)<k:
            heappush(heap,nums[b])
        elif nums[b]>heap[0]:
            heapreplace(heap,nums[b])
    else:
        if nums[b] in heap:
            print("YES")
        else:
            print("NO")