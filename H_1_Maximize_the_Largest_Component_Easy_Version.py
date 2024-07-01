for _ in range(int(input())):
    n,m = map(int,input().split())
    nums=[0]*m
    hash=0
    row=0
    for i in range(n):
        s = input()
        count=0
        for k in range(m):
            if s[k]==".":
                count+=1
                nums[k]+=1
            else:
                hash+=1
        row=max(row,count)
   
    added = max(nums)
    row=max(row,added)
    print(hash+row)
                