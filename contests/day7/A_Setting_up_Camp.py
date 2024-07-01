from math import ceil
for _ in range(int(input())):
    a,b,c= map(int,input().split())
    total = a+(b//3)
    mod = b%3
    tag=True
    if mod!=0:
        req=3-mod
        if req>c:
            tag=False
        else:
            total+=ceil((c-req)/3)+1
    
    else:
         total+=ceil((c)/3)
    
    if not tag:
        print(-1)
    else:
        print(total)