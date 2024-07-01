for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(1)
        print(1,2)
    else:
        if n%2==0:
            print(n//2)
        else:
            print(n//2+1)
        left=2
        right=6
        for i in range(n//2):
            print(left,right)
            left+=6
            right+=6
        if n%2==1:
            print(3*n-2,3*n-1)
        
        