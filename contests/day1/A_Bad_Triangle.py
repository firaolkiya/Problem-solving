for _ in range(int(input())):
    n = int(input())
    nums=list(map(int,input().split()))
    min1=0 if nums[0]<nums[2] else 1
    min2=int(not min1)
    right=2
    while right<n:
        if nums[right]<nums[min1]:
            min2=min1
            min1=right
        elif nums[right]<nums[min2]:
            min2=right
        elif nums[min1]+nums[min2]<=nums[right]:
            print(min(min1+1,min2+1),max(min1+1,min2+1),right+1)
            break
        right+=1
    else:
        print(-1)