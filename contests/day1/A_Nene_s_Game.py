for i in range(int(input())):
    n,q = map(int,input().split())
    nums= list(map(int,input().split()))
    amount=list(map(int,input().split()))
    ans=[]
    for i in range(q):
        ans.append(min(nums[0]-1,amount[i]))
    print(*ans)