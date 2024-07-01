for i in range(int(input())):
    a,b= map(int,input().split(" "))
    nums= list(map(int,input().split(" ")))
    product=1
    for num in nums:
        product*=num
    if 2023%product!=0:
        print("NO")
        continue
    remain= 2023//product
    divisor=[1]
    temp=remain
    k=2
    while temp>0:
        if temp%k==0:
            divisor.append(temp)
            temp/=k
        else:
            k+=1
        
    
    