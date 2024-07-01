t = int(input())  # number of test cases

for _ in range(t):
    x, y = map(int, input().split())  # read x and y

    z = x ^ y  # calculate x ⊕ y

    position = 0
    for i in range(31, -1, -1):
        if z & (1 << i):
            position = i + 1
            break

    length = 2 ** (position - 1)
    print(length)