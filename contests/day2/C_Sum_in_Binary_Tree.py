
def calculator(n):
    if n==1:
        return 1
    else:
        return n+calculator(n//2)
for _ in range(int(input())):
    depth=int(input())
    print(calculator(depth))
    