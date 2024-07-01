from bisect import bisect_right


for i in range(int(input())):
    n = int(input())
    nums= list(map(int,input().split()))
    nums.sort()
    mid=n//2
    if n%2==0 and mid>0:
        mid-=1
    m=bisect_right(nums,nums[mid])
    print(m-mid)