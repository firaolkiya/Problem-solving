for _ in range(int(input())):
    a,b,c = map(int,input().split())
    total=c//a+c//b+2
    print(total)