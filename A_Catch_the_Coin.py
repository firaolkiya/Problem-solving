for _ in range(int(input())):
    x,y = map(int,input().split())
    if y>=0:
        if y>=abs(x):
            print("YES")
        else:
            print("NO")
    else:
        if x<-1 or y<-1:
            print("NO")
        else:
            print("NO")