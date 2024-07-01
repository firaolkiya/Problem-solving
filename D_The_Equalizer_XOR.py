for _ in range(int(input())):
    n = int(input())
    nums =list(map(int,input().split()))
    left=[]
   
    for i in range(1,n):
        nums[i]^=nums[i-1]
    def isPossible(index):
        m=nums[index]
        for i in range(index+1,n):
            k=nums[i]^nums[index]
            if k==m:
                index=i
        return index==n-1
        
    
    for i in range(n-1):
        if isPossible(i):
            print("YES")
            break
    else:
        print("NO")
    
    
        