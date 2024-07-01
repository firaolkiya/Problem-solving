from os import name
import sys, threading


def main():
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        memo={}
        def dp(index):
            if index>=n:
                return 0
            if index not in memo:
                memo[index]=arr[index]+dp(index+arr[index])
            return memo[index]
        ans=0
        for i in range(n-1,-1,-1):
            ans=max(ans,dp(i))
        print(ans)

    
if name == 'main':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()