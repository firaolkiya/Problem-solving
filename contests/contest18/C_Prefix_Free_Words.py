from collections import defaultdict, deque

class TrieNode():
    def __init__(self):
        self.is_end=False
        self.children=[None,None]
        

n = int(input())
nums=list(map(int,input().split()))

root = TrieNode()
st=defaultdict(list)
for i in range(n):
    st[nums[i]].append(i)
ans=[]
nums.sort()
for num in nums:
    queue=deque()
    queue.append((root,[]))
    tag=True
    while queue:
        cur,path=queue.popleft()
        if path and len(path)==num and not cur.is_end:
            ans.append((st[num][-1],"".join(path)))
            st[num].pop()
            cur.is_end=True
            tag=False
            break
        if cur.children[0] is None and not cur.is_end:
            cur.children[0]=TrieNode()
            path.append("0")
            queue.append((cur.children[0],path))
        elif cur.children[1] is None and not cur.is_end:
            cur.children[1]=TrieNode()
            path.append("1")
            queue.append((cur.children[1],path))
        elif not cur.is_end:
            temp=path[::]
            path.append("1")
            temp.append("0")
            queue.append((cur.children[1],path))
            queue.append((cur.children[0],temp))
    if tag:
        ans=[]
        break
if not ans:
    print("NO")
else:
    print("YES")
    ans.sort()
    for a in ans:
        print(a[1])