import sys
input = sys.stdin.readline

n= int(input())
graph={i:i for i in range(1,n+1)}

def find(x):
    if graph[x]==x:
        return x
    return find(graph[x])
degree=[0]*(n+1)
def union(a,b):
    left=find(a)
    right=find(b)
    if degree[left]<degree[right]:
        graph[left]=right
    elif degree[right]<degree[left]:
        graph[right]=left
    else:
        graph[left]=right
        degree[left]+=1
    return True


for i in range(int(input())):
    a,b = map(int,input().split())
    if find(a)==find(b):
        print("cycle")
    else:
        union(a,b)