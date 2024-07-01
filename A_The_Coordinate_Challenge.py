for _ in range(int(input())):
    n = int(input())
    k = float('inf')
    if n%2==0:
        k=n//2
    m = n//3
    if(n%3==1):
        l = n-4
        l = l//3+2
        if(n>5):
            print(min(m+2,l,k))
        else:
            print(min(m+2,k))
    elif n%3==2:
        print(min(k,m+1))
    else:
        
        print(min(k,m))
    