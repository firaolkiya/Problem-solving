num = 10

subset = []
def search(n):
    if n==5:
        print(subset)
        return
    search(n+1)
    subset.append(n)
    search(n+1)
    subset.pop()
search(0)