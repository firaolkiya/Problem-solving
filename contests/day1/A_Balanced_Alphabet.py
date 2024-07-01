letter="abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    n, k = map(int,input().split())
    repeat = letter[:k]
    lis=repeat*(n//k)+letter[:n%k]
    print(lis)
    