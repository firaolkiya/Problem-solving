
for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split(" ")))
    count=0

    for num in nums:
        while num%2==0:
            num/=2
            count+=1
    t=0
    for i in range(n,0,-1):
        if count>=n:
            break
        temp=i
        while te%2==0:
            t+=1
            count+=i//2
    if count>=n:
        print(t)
    else:
        print(-1)