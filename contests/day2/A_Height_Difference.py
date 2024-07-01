n = int(input())
for _ in range(n):
    a,b= map(int,input().split())
    nums= list(map(int,input().split(" ")))
    nums.sort()
    left=0
    right=a
    tag=False
    while right<len(nums):
        if nums[right]-nums[left]<b:
            print("NO")
            tag=True
            break
        right+=1
        left+=1
    if not tag:
        print("YES")