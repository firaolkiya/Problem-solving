from collections import defaultdict
from math import gcd


n = int(input())

nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
store=defaultdict(int)
zero=0
for i in range(n):
    if nums1[i]==0 and nums2[i]==0:
        zero+=1
    elif nums1[i]==0:
        continue
    elif nums2[i]==0:
        store[0]+=1
    else:
        m=gcd(nums1[i],nums2[i])
        if nums2[i]<0:
            m*=-1
        store[(nums2[i]//m,nums1[i]//m)]+=1
if len(store)==0:
    print(zero)
else:
    print(max(store.values())+zero)