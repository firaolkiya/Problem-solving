for _ in range(int(input())):
    n =int(input())
    nu=list(input().split(" "))
    nums="".join(nu)
    prev=int(nums[0])
    left=1
    right=2
    t=True
    while right<=len(nums):
        temp=int(nums[left:right])
        while temp<prev and right<len(nums):
            right+=1
            temp=int(nums[left:right])
        if temp>=prev:
            prev=temp
            left=right
            right+=1
        else:
            t=False
            break
    if t:
        print("YES")
    else:
        print("NO")
            