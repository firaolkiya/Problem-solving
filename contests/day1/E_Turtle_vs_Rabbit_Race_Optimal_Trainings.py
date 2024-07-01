from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def bin_search(nums,left,right,n):
    best=n
    while right>left:
        mid=(left+right)//2
        if nums[mid]>n:
            right=mid-1
        elif nums[mid]==n:
            best=mid
            left=mid+1
        else:
            best=mid+1
            left=mid+1
    return max(1,best)   
            
            

for __ in range(int(input())):
    n = int(input())
    prefix=[0]*(n+1)
    nums= list(map(int,input().split()))
    for i in range(n):
        prefix[i+1]=nums[i]+prefix[i]
    k = int(input())
    ans=[]
    for _ in range(k):
        left,u = map(int,input().split())
        right=min(bin_search(prefix,left,n,u+prefix[left ]),n)
        ans.append(right)
    print(ans)
        
        