from bisect import bisect_left, bisect_right
from collections import Counter
lucky=[]
n =input()
leng=len(n)
def buildlucky(k,nums):
    if k>=leng:
        if nums.count("4")==nums.count("7"):
            lucky.append(int("".join(nums[:])))
        return 
    mat=["4","7"]
    for m in mat:
        nums.append(m)
    
        buildlucky(k+1,nums)
        nums.pop()
        
buildlucky(0,[])
lucky.sort()
index=bisect_left(lucky,int(n))
if index<0 or index>=len(lucky):
    temp="4"*(leng//2+1)+"7"*(leng//2+1)
    print(temp)
else:
    print(lucky[index])    

