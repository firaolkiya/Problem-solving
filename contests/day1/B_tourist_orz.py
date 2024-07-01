t = int(input())

for _ in range(t):
    n, z = map(int, input().split())
    a = list(map(int, input().split()))

    max_val = max(a)
    result = z

    for i in range(n):
        a[i] |= z
        max_val = max(max_val, a[i])

    print(max_val)