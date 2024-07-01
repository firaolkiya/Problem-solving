
n = int(input())
nums=list(map(int,input().split()))

fin = set()
for num in nums:
    while num>0:
        if num%2==0:
            num//=2
        elif num%3==0:
            num//=3
        else:
            fin.add(num)
            break
if len(fin)==1:
    print("Yes")
else:
    print("No")





"""flag=False
lest = lcm(*nums)
for num in nums:
    if (lest//num)%2!=0 and (lest//num)%3!=0 and lest!=num:
        print("No")
        flag=True
        break
if not flag:
    print("Yes")"""