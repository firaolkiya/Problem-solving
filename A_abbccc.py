n =int(input())
s = input()
ans = []
ind = 0

k =1
while ind<n:
    ans.append(s[ind])
    ind+=k
    k+=1
print("".join(ans))
    