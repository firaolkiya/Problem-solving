
from math import ceil


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    diff = []
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            diff.append(nums[i]-nums[i+1])
            nums[i+1]=nums[i]
    diff.sort(reverse=True)
    minus=0
    ans=0
    while diff:
        x=diff.pop()
        ans+=max(0,(len(diff)+2)*(x-minus))
        minus=x
    print(ans)
