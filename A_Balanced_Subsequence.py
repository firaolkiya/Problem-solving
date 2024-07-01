from typing import Counter


n,k = map(int,input().split())
s = input()
counter = Counter(s)

ans = float('inf')
for i in range(k):
    char = chr((65+i))
    if char in counter:
        ans = min(ans,counter[char])
    else:
        ans=0
        
print(ans*k)