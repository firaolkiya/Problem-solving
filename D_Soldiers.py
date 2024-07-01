for _ in range(int(input())):
    a,b = map(int,input().split())
    factor = [0]*(a+1)
    for i in range(2,a+1):
        
        k=i
        count=1
        while k<=a:
            factor[k]=max(count,factor[k])
            count+=1
            k*=2
            
    print(sum(factor[b+1:]))
            
            