import sys
input = sys.stdin.readline

##take input
n = int(input())
nums= list(map(int,input().split()))
order= list(map(int,input().split()))
order.reverse()

rep = {}

score = [0]*(n+1)


degree = [0]*(n+1)
def find(node):
    if rep[node]==node:
        return node
    rep[node]=find(rep[node])
    return rep[node]


def union(node):
    count=nums[node-1]
    if node-1 in rep and node+1 in rep:
        left=find(node-1)
        right=find(node+1)
        count+=score[left]
        count+=score[right]
        if degree[left]>degree[right]:
            rep[right]=rep[node]=left
            degree[left]+=degree[right]+1
            score[left]=count
        elif degree[left]<degree[right]:
            rep[left]=rep[node]=right
            degree[right]+=degree[left]+1
            score[right]=count
        else:
            rep[right]=rep[left]=rep[node]=node
            score[node]=count
    elif node-1 in rep:
        left=find(node-1)
        count+=score[left]
        score[left]=count
        rep[node]=left
        degree[left]+=1
        
    elif node+1 in rep:
        right=find(node+1)
        count+=score[right]
        score[right]=count
        rep[node]=right
        degree[right]+=1
    else:
        rep[node]=node
        degree[node]+=1
        score[node]=count
    return count


ans=[]
max_=0
for node in order:
    m=union(node)
    max_=max(m,max_)
    ans.append(max_)

for i in range(len(ans)-2,-1,-1):
    print(ans[i])
print(0)
        
