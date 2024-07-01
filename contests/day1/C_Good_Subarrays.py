for _ in range(int(input())):
    n = int(input())
    s=input()
    nums=[0]
    nums.extend(list(s))
    for i in range(1,len(nums)):
        nums[i]=int(nums[i])+nums[i-1]
    count=0
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]-nums[j]==i-j:
                count+=1
    print(count)
    