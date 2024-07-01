class TrieNode:
    def __init__(self) -> None:
        self.children = [None]*2

n = int(input())

nums= list(map(int,input().split()))

nums=[0]+nums

root = TrieNode()
xor_left=0

for num in nums:
    xor_left^=num
    bits=[0]*64
    temp=xor_left
    ind=1
    while temp>0:
        bits[-ind]=temp%2
        temp>>=1
        ind+=1
    cur=root
    for bit in bits:
        if not cur.children[bit]:
            cur.children[bit]=TrieNode()
        cur=cur.children[bit]

xor_right=0
ans=0
for i in range(n,0,-1):
    bits=[0]*64
    temp=xor_right
    ind=1
    while temp>0:
        bits[-ind]=temp%2
        temp>>=1
        ind+=1
    cur=root
    st=[]
    for bit in bits:
        if cur.children[1-bit]:
            cur=cur.children[1-bit]
            st.append("1")
        else:
            cur=cur.children[bit]
            st.append("0")
    ans=max(ans,int("".join(st),2))
    xor_right^=nums[i]
print(ans)
    





