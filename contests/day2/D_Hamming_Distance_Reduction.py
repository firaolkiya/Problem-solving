n = int(input())
s1=input()
s2= input()

dic = {}
ismatched=False
a,b=-1,-1
count=0
for i in range(n):
    if s1[i]!=s2[i]:
        dic[s1[i]]=i
for ch, index in enumerate(dic):
    if s2[index] in 
print(count)
print(a,b)