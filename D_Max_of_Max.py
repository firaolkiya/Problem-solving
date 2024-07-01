import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    
    prefix = [0]
    ans = 0
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            max_ = nums[i]+1+
            
            ans = max(ans,nums[i]+(k-prefix[-1]+1))
        prefix.append(nums[-1]+abs(nums[i]-nums[i-1]))
    print(ans)
            
