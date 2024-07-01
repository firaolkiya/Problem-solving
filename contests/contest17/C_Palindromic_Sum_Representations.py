

import sys

input = lambda: sys.stdin.readline().strip()


def isPalindore(n):
    k = str(n)
    return k==k[::-1]


mod=10**9+7
def solve():
    max_= 0
    inp = []
    for _ in range(int(input())):
        n = int(input())
        inp.append(n)
        max_ = max(max_,n)
    palind = [i for i in range(1,max_) if isPalindore(i)]
    dp = [0]*(max_+1)
    dp[0]=1
    for num in palind:
        for i in range(num,max_+1):
            dp[i]= (dp[i-num]+dp[i])%mod
                
    for k in inp:
        print(dp[k])


solve()
