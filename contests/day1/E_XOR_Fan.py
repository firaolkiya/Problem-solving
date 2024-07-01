import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n= int(input())
    nums= list(map(int,input().split()))
    s=input()
    zero=0
    one=0
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]^nums[i]
        if s[i]=="0":
            zero^=nums[i]
        else:
            one^=nums[i]
    
    k = int(input())
    ans=[]    
    for __ in range(k):
        tem=list(map(int,input().split()))
        if tem[0]==2 and tem[1]==0:
            ans.append(zero)
        elif tem[0]==2 and tem[1]==1:
            ans.append(one)
        else:
            temp=prefix[tem[2]]^prefix[tem[1]-1]
            one^=temp
            zero^=temp
    print(*ans)
        
    