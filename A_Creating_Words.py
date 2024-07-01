
for _ in range(int(input())):
    a,b= input().split()
    aa=list(a)
    bb= list(b)
    aa[0],bb[0]=bb[0],aa[0]
    print("".join(aa),"".join(bb))
    