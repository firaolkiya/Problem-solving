
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    
    ans=[]
    
    nums=[0]*32
    for i in range(n):
        m=bin(nums[i])
