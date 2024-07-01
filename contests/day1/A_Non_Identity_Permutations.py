n = int(input())
for i in range(n):
    a=int(input())
    ans=[]
    for i in range(2,a+1):
        ans.append(i)
    ans.append(1)
    print(*ans)