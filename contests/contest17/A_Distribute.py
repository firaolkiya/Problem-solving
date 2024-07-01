from collections import defaultdict


n = int(input())
nums= list(map(int,input().split()))
index=defaultdict(list)
for i in range(n):
    index[nums[i]].append(i+1)
nums.sort()
j=n-1
for i in range(n//2):
    print(index[nums[i]].pop(),index[nums[j]].pop())
    j-=1