for _ in range(int(input())):
    n = int(input())
    nums=list(map(int,input().split()))
    low=0
    high=0
    for num in nums:
        high=max(high+num,low+num,abs(low+num))
        low=num+low
    print(max(high,abs(low)))