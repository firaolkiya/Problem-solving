for _ in range(int(input())):
    a,b=map(int,input().split())
    list1  = list(map(int,input().split()))
    list2  = list(map(int,input().split()))
    new_map = zip(list1,list2)
    new_map = sorted(new_map)
    stack =[(0,0)]
    max_=0
    print(new_map)
    for num in new_map:
        while len(stack)>1 and stack[-1][1]+num[1]>b:
            stack.pop()
        temp=stack[-1]
        stack.append((num[0]+temp[0],num[1]+temp[1]))
        max_=max(max_,stack[-1][0])
    print(max_)
    