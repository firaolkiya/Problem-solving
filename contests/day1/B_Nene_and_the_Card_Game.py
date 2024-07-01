for _ in range(int(input())):
    n  =int(input())
    nums=list(input().split())
    s=set(nums)
    print(n-len(s))