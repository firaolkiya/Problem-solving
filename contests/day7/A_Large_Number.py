for _ in range(int(input())):
    size,digit=input().split()
    num=input()
    ans=""
    for i in range(int(size)):
        if num[i]<digit:
            ans=num[:i]+digit+num[i:]
            break
    else:
        ans=num+digit
    print(ans)