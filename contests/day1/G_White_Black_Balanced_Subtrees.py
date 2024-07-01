from os import name
import sys, threading


def main():
    n,a,b,c=map(int,input().split())

    nums=[a,b,c]

    memo={}
    def dp(n,count):
        if n==0:
            return count
        if n<0:
            return -1
        if n not in memo:
            memo[n-a]=dp(n-a,count+1)
            memo[n-b]=dp(n-b,count+1)
            memo[n-c]=dp(n-c,count+1)
            memo[n]=max(memo[n-c],memo[n-a],memo[n-b])
        return memo[n]
    print(dp(n,0))

    
if name == 'main':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()