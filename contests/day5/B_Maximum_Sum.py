from math import ceil


for _ in range(int(input())):
    a,b = map(int,input().split())
    nums=list(map(int,input().split()))
    maxSum=float('-inf')
    
    minfromLeft=0
    runSum=0
    for i in range(a):
        runSum+=nums[i]
        maxSum=max(maxSum,runSum-minfromLeft)
        minfromLeft=min(minfromLeft,runSum)
    k=2**(b)
    mod=10**9+7
    if maxSum<0:
        x=abs(ceil(runSum/mod))
        x=max(x+1,1)
        print(mod*x+runSum)
    else:
        print(((maxSum)*k-(maxSum-runSum))%mod)