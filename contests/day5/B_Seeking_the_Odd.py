from cmath import sqrt


for _ in range(int(input())):
    n=int(input())
    div=2
    flag=False
    while n>1 and not flag:
        if n%2==1 :
            flag=True
        while n%div==0:
            n//=div
            if div%2==1:
                flag=True
                break
        div+=1
    if flag:
        print("YES")
    else:
        print("NO")