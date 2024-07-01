n,k = map(int,input().split())

nums=list(map(int,input().split()))

def dp(index,part,count):
    if index==n:
        if part==k:
            return count*part
        else:
            return float('-inf')
    if part>k:
        return  float('-inf')
    
    m1=dp(index+1,part,count+nums[index])
    m2=count*part+dp(index+1,part+1,0)
    return max(m1,m2)
print(dp(0,1,nums[0]))
    