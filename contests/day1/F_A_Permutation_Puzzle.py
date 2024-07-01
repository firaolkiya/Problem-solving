
from collections import defaultdict
from math import lcm

def helper(string):
    for i in range(1,len(string)+1):
        set1 =set()
        for j in range(0,len(string),i):
            set1.add(string[j:j+i])
            if len(set1)>1:
                break
        if len(set1)==1:
            return i
    return len(string)
    
for _ in range(int(input())):
    n = int(input())
    s = input()
    nums = list(map(int,input().split()))
    graph = defaultdict(int)
    for i in range(n):
        graph[i+1]=nums[i]
    
    visited= set()
    subGraph=[]
    for node in range(1,n+1):
        if node not in visited:
            temp=[]
            moved = set()
            source=node
            while source not in moved:
                temp.append(s[source-1])
                moved.add(source)
                visited.add(source)
                source=graph[source]
            subGraph.append(temp[::])
    m = []
    for k in subGraph:
        kk= "".join(k)
        m.append(helper(kk))
    res=1
    for ele in m:
        res=lcm(res,ele)
    print(res)
                
            
        
        
    