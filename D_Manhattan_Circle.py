

for _ in range(int(input())):
    row,col = map(int,input().split())
    top,bottom=row,1
    left,right=col,1
    for i in range(row):
        m = input()
        for j in range(col):
            if m[j]=="#":
                top = min(i,top)
                left = min(j,left)
                bottom = max(bottom,i)
                right = max(right,j)
    print(top+(bottom-top)//2+1,left+(right-left)//2+1)