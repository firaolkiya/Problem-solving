from math import factorial


n = int(input())
a = input()
factr = [factorial(i) for i in range(10)]
target = 1
for s in a:
    target*=factr[int(s)]

ans=[]
def back(lis):
    su = 1
    for k in lis:
        su*=factr[int(k)]
    if(su==target) and lis:
        ans.append(int("".join(lis)))
        return True
    if(su>target):
        return False
    for i in range(9,1,-1):
        m = [kk for kk in lis]
        m.append(str(i))
        back(m)
    return False
back([])
print(max(ans))
        

    