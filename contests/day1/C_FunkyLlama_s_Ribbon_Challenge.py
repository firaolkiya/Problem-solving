from os import name
import sys, threading


def main():
    n,a,b,c=map(int,input().split())

    nums=[a,b,c]

    memo={}
    def dp(index,count):
        if count==n:
            return 0
        if n<0:
            return float('-inf')
        dp(index,count+nums[index])
        dp(index+1,count)
        mem
    print(dp(n,0))

    
if name == 'main':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()  