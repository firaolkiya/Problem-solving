for _ in range(int(input())):
    s = input()
    ans=["0"]*(len(s)*2)
    
    left=0
    right=len(s)*2-1
    for i in range(len(s)):
        ans[left]=s[i]
        ans[right]=s[i]
        left+=1
        right-=1
    print("".join(ans))