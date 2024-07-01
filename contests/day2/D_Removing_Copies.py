from collections import Counter

a,b = map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
count=Counter(arr)

count = dict(sorted(count.items() key=lambda item: item[1]))
print(count)