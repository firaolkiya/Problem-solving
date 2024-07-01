
from collections import defaultdict


n = int(input())
nums = list(map(int,input().split()))
k = int(input())

full  = set()
vassel = [[[0,n]*2] for i in range(n+1)]
for i in range(1,n):
    vassel[i][1]=i+1
    vassel[i+1][0]=i

    
    
vassel[n]=n

def find(x):
    return vassel[x]
def union(val,index):
    
    vassel[index]+=val
    
    
    
    

for i in range(k):
    op,lis = map(int,input().split())
    