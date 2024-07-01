
from math import ceil
from typing import Counter


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    
    pizza = Counter(nums)
    p = [[pizza[c], c] for c in pizza]
    p.sort(key=lambda x: (-x[0], x[1]))
    print(p)
   
    nums.sort(reverse=True)
    
    count=0
    deleted=set()
    visited=set()
    while nums:
        while nums and nums[-1] in visited:
            nums.pop()
        if nums and nums[-1]:
            visited.add(nums[-1])
            count+=1  
        
        while p and p[-1][1] in visited:
            p.pop()
        if p:
            p[-1][0]-=1
            print(p)
            if p[-1][0]==0:
                visited.add(p[-1][1])
                p.pop()
    print(count)
        