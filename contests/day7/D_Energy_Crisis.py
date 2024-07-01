size,lost = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()


def ispossible(energy):
    total_energy =sum(nums)
    
    for i in nums:
        
        if i>=energy:
            total_energy-=energy
        else:
            x=energy-i
            reducing = round(((100*x)/(100-lost)+i),6)
            total_energy-=reducing
        
        
    return round(total_energy,6)
        
left,right,best=nums[0],nums[-1],0
while left<=right:
    mid=round((left+right)/2,6)
    t=ispossible(mid)
    if t<0:
        right=mid-0.000001
    elif t==0:
        best=mid
        break
    else:
        best=mid
        left=mid+0.000001
print(best)