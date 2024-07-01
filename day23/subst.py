num = 10

# def search(n):
#     if n==5:
#         print(subset)
#         return
#     search(n+1)
#     subset.append(n)
#     search(n+1)
    
# search(0)

for bits in range(1<<5):
    subset=[]
    for bit in range(5):
        if (1<<bit) & bits:
            subset.append(bit)
    print(subset)