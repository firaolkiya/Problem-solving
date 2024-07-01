leng = int(input())
s=input()
letter={"a","i","e","o","u","y"}

ans=[s[0]]

for i in range(1,leng):
    if s[i] in letter and s[i-1] in letter:
        continue
    ans.append(s[i])
print("".join(ans))