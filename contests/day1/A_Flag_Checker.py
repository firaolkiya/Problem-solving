
n, m = map(int,input().split())

prev=""
flag=True
for i in range(n):
    row=input()
    x=set(row)
    if len(x)>1:
        flag=False
    if row[0]==prev:
        flag=False
    prev=row[0]
    
if flag:
    print("YES")
else:
    print("NO")

        