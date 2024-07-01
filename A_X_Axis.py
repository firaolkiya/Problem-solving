for _ in range(int(input())):
    nums = list(map(int,input().split()))
    nums.sort()
    ans=float('inf')
    for num in range(nums[0],nums[2]+1):
        temp = abs(num-nums[0])+abs(num-nums[1])+abs(num-nums[2])
        ans = min(ans,temp)
    print(ans)