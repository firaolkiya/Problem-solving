n =int(input())

nums = list(map(int,input().split()))

stack= []
long=0
for num in nums:
    
    if stack and num<=stack[-1]:
        stack=[]
    stack.append(num)
    long=max(long,len(stack))
print(long)