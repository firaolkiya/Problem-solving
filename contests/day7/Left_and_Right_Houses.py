for _ in range(int(input())):
    n = int(input())
    s=input()
    prefix=[0]*(n)
    suffix=[0]*n
    sum_=0
    Sum=0
    index=0
    for i in range(n):
        sum_+=int(s[i]=="0")
        Sum+=int(s[i])
        prefix[i]+=sum_
        suffix[i]+=Sum
    print(prefix)
    for i in range(n):
        agreeL=prefix[i]
        agreeR=suffix[-1]-suffix[i]
        totL=i+1
        if agreeL>=totL/2 and agreeR>=(n-totL)/2:
            if i==0:
                index=1
                continue
            print(agreeL,agreeR)
            pre_distance=abs(n/2-index)
            cur_distance = abs(n/2-i-1)
            if cur_distance<pre_distance and prefix[i]!=prefix[i-1]:
                index=i+1
    print(index)
    
    
    
