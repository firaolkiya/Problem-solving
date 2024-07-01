
from heapq import heappop, heappush, heapreplace


n = int(input())
nums = list(map(int,input().split()))

heap = []
count=0
sum=0
for num in nums:
    if sum+num<0:
        if heap and heap[0]<num:
            sum+=num-heap[0]
            if num>0:
                heappop(heap)
            else:
                heapreplace(heap,num)
    elif sum+num>=0:
        sum+=num
        count+=1
        if num<0:
            heappush(heap,num)
        

print(count)
    
    

# memo={}
# def dp(index,health):
#     if index>=n or health<0:
#         return 0
#     if not (index,health) in memo:
#         l=dp(index+1,health)
#         r=0
#         if health+nums[index]>=0:
#             r=dp(index+1,health+nums[index])+1
#         memo[(index,health)]=max(l,r)
#     return memo[(index,health)]
# print(dp(0,0))