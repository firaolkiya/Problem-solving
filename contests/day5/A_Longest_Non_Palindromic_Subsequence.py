
def isPalindrome(s):
    right,left=len(s)-1,0
    while left<right:
        if s[left]!=s[right]:
            return False
        right-=1
        left+=1
    return True
for _ in range(int(input())):
    s=input()
    left,right=0,len(s)-1
    ans=-1
    while left<right:
        if not isPalindrome(s[left:]):
            ans=right-left+1
            break
        left+=1
    while left<right:
        if not isPalindrome(s[:right+1]):
            ans=max(ans,right-left+1)
            break
        right-=1
   
    print(ans)