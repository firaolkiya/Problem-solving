def calc(n,b):
    if n>b or n<1:
        return False
    if n==b:
        return True
    left=False
    if n%2==0 and n>2:
        left=calc((n//2)*3,b)
    right=calc(n*3,b)
    return right or left

for i in range(int(input())):
    pile,fin =map(int,input().split())
    if calc(fin,pile):
        print("YES")
    else:
        print("NO")
    