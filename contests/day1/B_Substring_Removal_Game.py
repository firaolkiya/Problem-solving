for _ in range(int(input())):
    s=input()
    left,right=0,0
    nums=[0]
    while right<len(s):
        if s[left]=="0":
            left+=1
        elif s[right]=="0":
            nums.append(right-left)
            left=right
        right+=1
    if s[-1]=="1":
        nums.append(right-left)
    nums.sort(reverse=True)
    sum=0
    for i in range(0,len(nums),2):
        sum+=nums[i]
    print(sum)