for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    
    max_=0
    sum_=0
    count=0
    for i in range(n):
        max_ = max(max_,nums[i])
        sum_+=nums[i]
        if sum_ - max_ == max_:
            count+=1
    print(count)