a,b = map(int,input().split(" "))
nums= list(map(int,input().split(" ")))
right=0
total=0
count=0
left=0
while right<a:
    total+=nums[right]
    while total>b and left<right:
        total-=nums[left]
        left+=1
    if total<=b:
        count=max(count,right-left+1)
    right+=1
print(count)