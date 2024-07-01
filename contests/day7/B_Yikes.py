from bisect import bisect_left


n= int(input())
nums= list(map(int,input().split(" ")))
size=int(input())
worms= list(map(int,input().split(" ")))
prefix=[]
sum_=0
for i in range(n):
    sum_+=nums[i]
    prefix.append(sum_)
for num in worms:
    print(bisect_left(prefix,num)+1)
