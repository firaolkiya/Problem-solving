from math import ceil


for i in range(int(input())):
    s=input()
    le=len(s)
    mid=ceil(le/2)
    s1=s[:mid]
    s2=s[mid:]
    if s1==s2:
        print("YES")
    else:
        print("NO")