for _ in range(int(input())):
    n = int(input())
    nums=list(map(int,input().split()))
    p=[]
    mex=0
    temp=set()
    for i in range(n):
        while mex-nums[i]<0 or mex-nums[i] in temp:
                mex+=1
        p.append(mex-nums[i])
        temp.add(p[-1])
    print(*p)
    