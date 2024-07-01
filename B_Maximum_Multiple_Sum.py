for _ in range(int(input())):
    d = int(input())
    ans=0
    num = 0
    for i in range(2,d+1):
        n= d//i
        sum_=0
        p=i
        for k in range(n):
            sum_+=p
            p+=i
        if sum_>=ans:
            ans=sum_
            num = i
    print(num)
        