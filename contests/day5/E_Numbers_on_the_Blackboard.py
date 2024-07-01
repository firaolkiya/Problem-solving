
from collections import defaultdict
from math import gcd

for _ in range(int(input())):
    a,k=map(int,input().split())
    nums=list(map(int,input().split()))
    
    di = set()
    for i in range(a):
        nums[i]-=k
        if nums[i]<0:
            di.add(-1)
        elif nums[i]>0:
            di.add(1)
        else:
            di.add(0)
    if len(di)==1:
        if nums[0]==0:
            print(0)
        else:
            count=0
            gc=gcd(*nums)
            for num in nums:
                count+=abs(num//gc)-1
            print(count)
    else:
        print(-1)