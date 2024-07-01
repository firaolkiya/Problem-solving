n,m,k = [int(i) for i in input().split()]
nums = []
for _ in range(m):
    nums.append(int(input()))
fedro = int(input())
ct = 0
for n in nums:
    temp = n
    fd = fedro
    diff  =0
    while temp or fd:
        if temp%2 != fd%2:
            diff += 1
        temp>>=1
        fd>>=1
    if diff <= k:
        ct += 1
print(ct)           