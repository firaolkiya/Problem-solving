from cmath import sqrt

n,k = map(int,input().split())
nums= list(map(int,input().split()))
def function(ind):
    if n==1:
        return sqrt(nums[ind-1])
    else:
        return sqrt(function(ind-1)+nums[ind])