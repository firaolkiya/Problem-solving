from math import ceil


def getTime(nums,yero,size):
    time=0
    for i in range(len(nums)):
        time+=ceil(nums[i]/size)*yero[i]
    return time

for _ in range(int(input())):
    n,k = map(int,input().split())
    nums=list(map(int,input().split()))
    yero=list(map(int,input().split()))
    left,right,best=1,max(nums),-1
    
    while left<=right:
        mid=(left+right)//2
        if getTime(nums,yero,mid)>k:
            left=mid+1
        else:
            right=mid-1
            best=mid
    print(best)
    