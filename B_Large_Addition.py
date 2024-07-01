from collections import deque

for _ in range(int(input())):
    n = input()
    digit = ["5", "6", "7", "8", "9"]

    def is_correct(moving):
        f = int("".join(moving))
        x = str(int(n) - f)
        if len(x) != len(moving):
            return False
        for c in x:
            if c not in digit:
                return False
        return True

    queue = deque()
    is_got = False
    visited = set()
    moving = []
    t=True
    while queue or  t:
        t=False
        if moving and is_correct(moving):
            is_got = True
            break
        for d in digit:
            moving.append(d)
            x = int("".join(moving))
            if x < int(n) and x not in visited:
                queue.append(moving.copy())
                visited.add(x)
            moving.pop()

    if is_got:
        print("YES")
    else:
        print("NO")