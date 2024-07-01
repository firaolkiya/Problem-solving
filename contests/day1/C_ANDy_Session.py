t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    max_and = 0

    for bit in range(30, -1, -1):
        count = 0
        for i in range(n):
            if a[i] & (1 << bit)==0:
                count += 1

        if count <= k:
            max_and |= (1 << bit)
            k -= count

    print(max_and)