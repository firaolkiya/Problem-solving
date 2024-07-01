

from collections import defaultdict

for _ in range(int(input())):
    count=0
    dic ={}
    n =int(input())
    s=input()
    for i in range(n):
        if s[i] in dic:
            count+=i-dic[s[i]]
        dic[s[i]]=i
    for key in dic:
        count+=n-dic[key]
    print(count)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    