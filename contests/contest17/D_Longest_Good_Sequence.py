
from math import gcd


n =int(input())
nums = list(map(int,input().split()))

dp = [1]*(n)

for i in range(n-2,-1,-1):
    for k in range(i+1,n):
        if gcd(nums[i],nums[k])>1:
            dp[i]=dp[k]+1
            break
print(dp)
print(max(dp))
