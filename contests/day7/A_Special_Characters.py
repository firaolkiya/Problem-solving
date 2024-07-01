kk=["AA","BB"]
for i in range(int(input())):
    n =int(input())
    lis=[]
    if n%2==1:
        print("NO")
    else:
        for k in range(n//2):
            lis.append(kk[k%2])
        print("YES")
        print("".join(lis))