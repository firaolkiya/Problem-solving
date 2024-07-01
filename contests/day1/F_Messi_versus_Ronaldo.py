import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n=  int(input())
    nums=list(map(int,input().split()))
    
    new=[0]*60

    for i in range(n):
        temp=nums[i]
        q=0
        while temp>0:
            new[q]+=temp%2
            temp//=2
            q+=1

    
    