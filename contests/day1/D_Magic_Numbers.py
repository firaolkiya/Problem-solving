
from math import ceil


def isMagic(s,d):
    for i in range(1,len(s),2):
        if s[i]!=str(d):
            return False
    for i in range(0,len(s),2):
        if s[i]==str(d):
            return False
    return True

m,k=map(int,input().split())
a=int(input())
b=int(input())
start=ceil(a/m)*m
count=0
while start<=b:
    if isMagic(str(start),k):
        count+=1
    start+=m

print(count)
