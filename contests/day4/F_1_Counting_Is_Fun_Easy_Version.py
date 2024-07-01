def perm(a,b):
    s=1
    while b>0 and a>0:
        s+=a    
        a-=1
        b-=1
    return s
for _ in range(int(input())):
    leng,t,p=map(int,input().split())
    temp=0
    for i in range(t,-1,-1):
        temp+=(perm(i,leng-2))
    print(temp)