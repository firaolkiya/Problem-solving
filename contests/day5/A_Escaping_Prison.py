for _ in range(int(input())):
    n,h=map(int,input().split())
    total=0
    for i in range(n):
        a,b=map(int,input().split())
        total+=max(a,b)
    if total>=h:
        print("YES")
    else:
        print("NO")

        