from heapq import *
import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    heap=[]
    for i in range(n):
        heappush(heap,(-nums[i],i+1))
    ans=[]
    while len(heap)>1:
        k,ind1=heappop(heap)
        if heap[0][0]<-1:
            b,ind2=heapreplace(heap,(heap[0][0]+1,heap[0][1]))
        else:
             b,ind2=heappop(heap)
        if b<0 and k<0:
            ans.append((ind1,ind2))
        if k<0:
            heappush(heap,(k+1,ind1))
    print(len(ans))
    for i, j in ans:
        print(i,j)