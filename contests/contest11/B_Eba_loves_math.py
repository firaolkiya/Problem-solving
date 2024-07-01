t = int(int(input()))

for _ in range(t):
    
    n = int(input())
    nums = list(map(int,input().split()))
    
    lar = max(nums)
    for num in nums:
        lar&=num
    print(lar)