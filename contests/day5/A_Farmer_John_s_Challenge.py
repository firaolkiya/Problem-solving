for _ in range(int(input())):
    n ,k = map(int,input().split())
    ans=[]
    if n%k!=0:
        print(-1)
    elif k==1:
        ans=[i for i in range(n,0,-1)]
        print(*ans)
    else:
        temp=[i for i in range(1,k+1)]
        for i in range(n//k):
            ans.extend(temp)
        print(*ans)