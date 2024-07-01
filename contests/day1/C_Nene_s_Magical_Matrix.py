from math import ceil
import sys
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    mid=n//2
    sum1=((n*(n+1)//2)*(mid))
    print(sum1,mid)
    sum2=n*(n-mid)*(mid+2)//2
    print(sum1+sum2)