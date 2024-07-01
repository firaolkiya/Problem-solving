for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    ans=float('inf')
    for i in range(1,n):
        m = max(nums[i-1],nums[i])
        ans=min(m,ans)
    print(ans-1)
