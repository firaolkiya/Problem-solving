from collections import Counter


for _ in range(int(input())):
    a = input()
    b = input()
    m = Counter(a)
    n = Counter(b)
    
    ans = 0
    for char in m:
        ans+=m[char]
        if char in n:
            l= min(m[char],n[char])
            n[char]-=l
    for char in n:
        ans+=n[char]
    print(ans)