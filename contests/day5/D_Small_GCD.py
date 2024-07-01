from math import gcd


for _ in range(int(input())):
    n = int(input())
    nums=list(map(int,input().split(" ")))
    nums.sort()
    count=0
    comb = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            comb.append([nums[i],nums[j],n-j-1])
    for num in comb:
        count+=(gcd(num[0],num[1])*num[2])
    
    print(count)