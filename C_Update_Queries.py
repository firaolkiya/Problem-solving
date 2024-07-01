from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input().strip()
    s= list(s)
    nums = list(map(int,input().split()))
    t = input().strip()
    t= list(t)
    t.sort(reverse=True)
    nums.sort(reverse=True)
    modified = [False]*n
    while t and nums:
        char = t.pop()
        ind = nums.pop()
        if not modified[ind-1]:
            s[ind-1]=char
            modified[ind-1]=True
        else:
            t.append(char)
    print("".join(s))
        