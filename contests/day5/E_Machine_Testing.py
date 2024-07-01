from math import ceil


for _ in range(int(input())):
    n = int(input())
    health= list(map(int,input().split()))
    power= list(map(int,input().split()))
    
    stack = []
    total=0
    for i in range(1,n):
        t=0
        while stack and health[i]>0:
            if stack[-1][1]*stack[-1][0]>=health[i]:
                temp=ceil(health[i]/stack[-1][0])
                t+=temp
                stack[-1][1]-=temp
                health[i]=0
                if stack[-1][1]<=0:
                    stack.pop()
            else:
                t+=stack[-1][1]
                health[i]-=stack[-1][1]*stack[-1][0]
                stack.pop()
        if  not stack and health[i]>0:
            temp=ceil(health[i]/power[0])
            t+=temp
            total+=temp
        stack.append([power[i],t])
     
    print(total)
            
        
            
        