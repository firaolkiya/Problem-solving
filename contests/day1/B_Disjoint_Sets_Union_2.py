from collections import defaultdict
import sys
input = sys.stdin.readline

n, ins = map(int,input().split())

parent={i:i for i in range(n+1)}
size=[0]*(n+1)
graph = defaultdict(list)
def find(node):
    if node==parent[node]:
        return node
    parent[node]=find(parent[node])
    return parent[node]
def union(x,y):
    parentX=find(x)
    parentY=find(y)
    if size[parentX]>size[parentY]:
        parent[parentY]=parentX
        graph[parentX].append(parentY)
    elif size[parentY]>size[parentX]:
        parent[parentX]=parentY
        graph[parentY].append(parentX)
    else:
        parent[parentX]=parentY
        graph[parentY].append(parentX)
        size[parentY]+=1

for _ in range(ins):
    temp=input()
    if temp[:3]=="get":
        o,value=temp.split()
        p=find(int(value))
        max_=value
        min_=value
        count=1
        for k in graph[value]:
            min_=min(min_,k)
            max_=max(max_,k)
            count+=1
        print(min_,max_,count)
    else:
        op,value,l=temp.split()
        union(int(value),int(l))
print(graph)