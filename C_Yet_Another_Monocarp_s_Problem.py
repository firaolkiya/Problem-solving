for _ in range(int(input())):
    n,h = map(int,input().split())
    nums =list(map(int,input().split()))
    
    left=1
    right = h
    ans=0
    while right>=left:
        mid = (left+right)//2
        damaged=mid
        for i in range(n-1):
            damaged+=min(mid,nums[i+1]-nums[i])
        if damaged>=h:
            right=mid-1
            ans=mid
        else:
            left=mid+1
    print(ans)