for _ in range(int(input())):
    n=int(input())
    k=1
    
    while n & k==0:
        k<<=1
    
    if k^n>0:
        print(k)
    else:
        if k==1:
            print(3)
        else:
            print(k^1)