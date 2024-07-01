n =int(input())
s=input()
temp=list(s)
for i in range(1,n):
    if (n)%(i+1)==0:
        pre = temp[:i+1]
        pre.reverse()
        suff=temp[i+1:]

        temp=(pre+suff)
print("".join(temp))    

