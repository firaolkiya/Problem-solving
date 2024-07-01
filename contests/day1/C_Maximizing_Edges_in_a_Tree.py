from collections import defaultdict
from os import name
import sys
from sys import setrecursionlimit, stdin
import threading
input = sys.stdin.readline

def main():
    n = int(input())
    graph =defaultdict(list)
    for i in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited =set()
    color=[-1]*n
    col=[1,0]
    visited.add(1)
    def dfs(node,color):
        
        for child in graph[node]:
            if not child in visited:
                visited.add(child)
                if color==0:
                    col[0]+=1
                    dfs(child,1)
                else:
                    col[1]+=1
                    dfs(child,0)
            
    dfs(1,1)
    print(col[0]*col[1]-n+1)

if name == 'main':
    setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()
                
    

    
