def ispalindrome(s):
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
for _ in range(int(input())):
    leng,test=map(int,input().split())
    s=input()
    prefix=[0]*(leng+2)
    for i in range(leng):
        for j in range(i):
            if not ispalindrome(s[j:i+1]):
                prefix[j+1]+=i-j+1
                prefix[i+2]-=i-j+1

    for k in range(1,leng+2):
        prefix[k]+=prefix[k-1]
    print(prefix)
    for m in range(test):
        left,right=map(int,input().split())
        print(prefix[right]-prefix[left-1])
