for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
   
    stack=["B","R"]
    red=False
    max_=nums[0]
    for i in range(2,n):
        stack.append("B")
        max_=nums[i]
    if max_-nums[0]==0:
        print("NO")
    else:
        print("YES")
        print("".join(stack))
        