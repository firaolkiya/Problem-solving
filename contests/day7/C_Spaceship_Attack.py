from bisect import bisect_left



size,test = map(int,input().split())
nums= list(map(int,input().split()))
po_gold=[]
sum_=0


for i in range(test):
    a,b=map(int,input().split())
    po_gold.append([a,b])
    
##sort based on thier power  
po_gold.sort()
##calculate prefix sum of gold
for k in po_gold:
    sum_+=k[1]
    k[1]=sum_
    
def getGold(num):
    left,right,best=0,len(po_gold)-1,-1
    while left<=right:
        mid=(left+right)//2
        if po_gold[mid][0]>num:
            right=mid-1
        else:
            best=mid
            left=mid+1
    if best==-1:
        return 0
    return po_gold[best][1]

ans=[]
for i in range(size):
    ans.append(getGold(nums[i]))

print(*ans)