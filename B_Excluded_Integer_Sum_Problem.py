for _ in range(int(input())):
    n,k,x = map(int,input().split())

    if(x!=1):
        print("YES")
        print(n)
        l = ["1" for i in range(n)]
        print(" ".join(l))
    else:
       lis= []
       if((n%2==1 and k<3) or k<2):
           print("NO")
       elif n%2==0:
           print("YES")
           l = ["2" for i in range(n//2)]
           print(n//2)
           print(" ".join(l))
       else:
           print("YES")
           m = n//2-1
           print(n//2)
           l = ["2" for i in range(m)]
           l.append("3")
           print(" ".join(l))
           