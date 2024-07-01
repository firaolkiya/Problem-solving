
for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(2*n-1):
        if s[i]==")" and s[i+1]=="(":
            n-=1
    print(n)
   