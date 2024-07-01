
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    waiting =[0]*n
    ans=nums[-1]
    for i in range(n-2,-1,-1):
        d =nums[i+1]+1-nums[i]
        waiting[i]=max(0,waiting[i+1]+d)
        ans=max(ans,waiting[i]+nums[i])
    print(ans)
    