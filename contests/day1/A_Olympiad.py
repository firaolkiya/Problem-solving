n = int(input())
nums=list(map(int,input().split()))
lis=set(nums)
if 0 in lis:
    print(len(lis)-1)
else:
    print(len(lis))