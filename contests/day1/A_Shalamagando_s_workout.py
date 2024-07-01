
n = int(input())
nums = list(map(int,input().split()))

sp = [-1,-1,-1]
for i in range(n):
    sp[i%3]+=nums[i]
if max(sp)==sp[0]:
    print("chest")
elif max(sp)==sp[1]:
    print("biceps")
else:
    print("back")
    
 