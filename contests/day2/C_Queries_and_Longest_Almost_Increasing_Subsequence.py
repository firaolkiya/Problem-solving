a,b =map(int,input().split(" "))

nums=list(map(int,input().split(" ")))
def checker(left,right):
    for i in range(left,right-1):
        if nums[i]>=nums[i-1] and nums[i+1]>=nums[i]:
            return False
    return True
for i in range(b):
    x,y = map(int,input().split())
