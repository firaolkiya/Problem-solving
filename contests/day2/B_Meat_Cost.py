n = int(input())
sum=0
min_p=float('inf')
for  _ in range(n):
    a,p = map(int,input().split(" "))
    min_p=min(min_p,p)
    sum+=a*(min_p)
print(sum)