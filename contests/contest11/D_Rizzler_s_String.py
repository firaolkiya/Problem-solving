s = input()

a=0
b=0
ans=0
for i in range(len(s)):
    if s[i]=="a":
        a+=1
        ans+=b+1
    if s[i]=="b":
        b=a
print(ans)